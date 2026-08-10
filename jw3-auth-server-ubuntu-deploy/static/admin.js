/**
 * JW3 授权管理系统 - 前端JavaScript
 */

// 全局变量
let currentSection = 'dashboard';
let refreshInterval = null;

// 页面加载完成后初始化
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
});

// 初始化应用
function initializeApp() {
    console.log('初始化应用...');
    setupEventListeners();

    // 确保仪表板section显示
    console.log('切换到仪表板...');

    // 设置默认数据，避免空白
    const elements = ['total-licenses', 'active-licenses', 'total-clients', 'online-clients'];
    elements.forEach(id => {
        const element = document.getElementById(id);
        if (element && (element.textContent === '-' || element.textContent.trim() === '')) {
            element.textContent = '0';
        }
    });

    // 设置系统状态
    const systemStatus = document.getElementById('system-status');
    if (systemStatus) {
        systemStatus.innerHTML = '<div class="alert alert-info">正在加载系统状态...</div>';
    }

    const recentActivity = document.getElementById('recent-activity');
    if (recentActivity) {
        recentActivity.innerHTML = '<div class="alert alert-info">正在加载最近活动...</div>';
    }

    switchSection('dashboard');

    toggleExpireSettings();
    toggleCreateLicenseTypeFields();

    // 加载许可证验证状态
    loadLicenseValidationStatus();

    // 显示一个测试消息
    setTimeout(() => {
        showAlert('管理界面已加载', 'success');
    }, 1000);

    startAutoRefresh();
}

// 设置事件监听器
function setupEventListeners() {
    // 侧边栏导航
    document.querySelectorAll('.sidebar .nav-link').forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const section = this.getAttribute('data-section');
            if (section) {
                switchSection(section);
            }
        });
    });

    // 移动端侧边栏切换
    const sidebarToggle = document.getElementById('sidebarToggle');
    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', function() {
            document.getElementById('sidebar').classList.toggle('show');
        });
    }

    // 点击主内容区域时隐藏移动端侧边栏
    document.querySelector('.main-content').addEventListener('click', function() {
        document.getElementById('sidebar').classList.remove('show');
    });
}

// 切换内容区域
function switchSection(section) {
    console.log('切换到section:', section);

    // 隐藏所有内容区域
    document.querySelectorAll('.content-section').forEach(el => {
        el.style.display = 'none';
    });

    // 移除所有导航链接的活跃状态
    document.querySelectorAll('.sidebar .nav-link').forEach(link => {
        link.classList.remove('active');
    });

    // 显示目标内容区域
    const targetSection = document.getElementById(section + '-section');
    console.log('目标section元素:', targetSection);
    if (targetSection) {
        targetSection.style.display = 'block';
        currentSection = section;
        console.log('已显示section:', section);
    } else {
        console.error('找不到section元素:', section + '-section');
    }

    // 激活对应的导航链接
    const activeLink = document.querySelector(`[data-section="${section}"]`);
    if (activeLink) {
        activeLink.classList.add('active');
    }

    // 加载对应的数据
    loadSectionData(section);
}

// 加载区域数据
function loadSectionData(section) {
    switch (section) {
        case 'dashboard':
            loadDashboard();
            break;
        case 'licenses':
            loadLicenses();
            break;
        case 'clients':
            loadClients();
            break;
        case 'users':
            loadUsers();
            break;
        case 'logs':
            loadLogs();
            break;
        case 'market':
            loadMarketPackages();
            break;
        case 'settings':
            loadSettings();
            break;
    }
}

// 加载仪表板数据
async function loadDashboard() {
    console.log('开始加载仪表板数据...');

    // 首先检查是否已登录
    try {
        const authCheck = await fetch('/api/admin/check_auth', {
            credentials: 'include'
        });
        console.log('认证检查状态:', authCheck.status);

        if (authCheck.status === 401) {
            console.log('用户未登录，重定向到登录页面');
            window.location.href = '/login';
            return;
        }
    } catch (error) {
        console.error('认证检查失败:', error);
    }

    try {
        // 并行加载所有API数据
        console.log('开始并行加载API数据...');
        const apiPromises = [
            fetch('/health'),
            fetch('/api/admin/licenses', { credentials: 'include', cache: 'no-cache' }),
            fetch('/api/admin/clients', { credentials: 'include', cache: 'no-cache' })
        ];

        const results = await Promise.allSettled(apiPromises);
        console.log('所有API调用完成:', results.map(r => r.status));

        // 处理健康检查数据
        if (results[0].status === 'fulfilled') {
            try {
                const healthResponse = results[0].value;
                console.log('健康检查响应状态:', healthResponse.status);
                const healthData = await healthResponse.json();
                console.log('健康检查数据:', healthData);

                if (healthData.statistics) {
                    document.getElementById('total-licenses').textContent = healthData.statistics.licenses || 0;
                    document.getElementById('total-clients').textContent = healthData.statistics.clients || 0;
                }
            } catch (error) {
                console.error('处理健康检查数据失败:', error);
            }
        } else {
            console.error('健康检查API调用失败:', results[0].reason);
        }

        // 处理许可证数据
        if (results[1].status === 'fulfilled') {
            try {
                const licensesResponse = results[1].value;
                console.log('许可证API响应状态:', licensesResponse.status);

                if (licensesResponse.status === 401) {
                    console.log('许可证API认证失败，重定向到登录页面');
                    window.location.href = '/login';
                    return;
                }

                const licensesData = await licensesResponse.json();
                console.log('许可证数据:', licensesData);

                if (licensesData.success) {
                    const activeLicenses = licensesData.licenses.filter(l => l.is_active).length;
                    document.getElementById('active-licenses').textContent = activeLicenses;
                } else {
                    document.getElementById('active-licenses').textContent = '0';
                }
            } catch (error) {
                console.error('处理许可证数据失败:', error);
                document.getElementById('active-licenses').textContent = '0';
            }
        } else {
            console.error('许可证API调用失败:', results[1].reason);
            document.getElementById('active-licenses').textContent = '0';
        }

        // 处理客户端数据
        if (results[2].status === 'fulfilled') {
            try {
                const clientsResponse = results[2].value;
                console.log('客户端API响应状态:', clientsResponse.status);

                if (clientsResponse.status === 401) {
                    console.log('客户端API认证失败，重定向到登录页面');
                    window.location.href = '/login';
                    return;
                }

                const clientsData = await clientsResponse.json();
                console.log('客户端数据:', clientsData);

                if (clientsData.success) {
                    // 计算在线客户端（最近24小时内活跃）
                    const now = new Date();
                    const onlineClients = clientsData.clients.filter(client => {
                        if (!client.last_seen) return false;
                        const lastSeen = new Date(client.last_seen);
                        const hoursDiff = (now - lastSeen) / (1000 * 60 * 60);
                        return hoursDiff <= 24;
                    }).length;

                    document.getElementById('online-clients').textContent = onlineClients;
                } else {
                    document.getElementById('online-clients').textContent = '0';
                }
            } catch (error) {
                console.error('处理客户端数据失败:', error);
                document.getElementById('online-clients').textContent = '0';
            }
        } else {
            console.error('客户端API调用失败:', results[2].reason);
            document.getElementById('online-clients').textContent = '0';
        }

        // 并行加载系统状态和最近活动
        Promise.allSettled([
            loadSystemStatus(),
            loadRecentActivity()
        ]).then(statusResults => {
            console.log('系统状态和活动加载完成:', statusResults.map(r => r.status));
        });

    } catch (error) {
        console.error('加载仪表板数据失败:', error);
        // 设置默认值，避免页面完全空白
        document.getElementById('total-licenses').textContent = '0';
        document.getElementById('active-licenses').textContent = '0';
        document.getElementById('total-clients').textContent = '0';
        document.getElementById('online-clients').textContent = '0';

        // 显示错误信息
        document.getElementById('system-status').innerHTML =
            '<div class="alert alert-warning">无法加载系统状态，请检查网络连接</div>';
        document.getElementById('recent-activity').innerHTML =
            '<div class="alert alert-warning">无法加载最近活动，请检查网络连接</div>';

        showAlert('加载仪表板数据失败: ' + error.message, 'warning');
    }
}

// 加载系统状态
async function loadSystemStatus() {
    try {
        const response = await fetch('/health', {
            credentials: 'include',
            cache: 'no-cache'
        });
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }
        const data = await response.json();

        const serviceStatus = String(data.status || '未知');
        const serviceBadgeClass = serviceStatus === '正常' ? 'bg-success' : 'bg-danger';
        const databaseConnected = data.database_connected !== false;
        const databaseStatus = String(data.database || (databaseConnected ? '已连接' : '异常'));
        const databaseBadgeClass = databaseConnected ? 'bg-success' : 'bg-danger';
        const uptimeSource = (data.uptime_seconds ?? data.startup_time ?? data.timestamp);

        const statusHtml = `
            <div class="row">
                <div class="col-md-6">
                    <div class="d-flex justify-content-between">
                        <span>服务状态:</span>
                        <span class="badge ${serviceBadgeClass}">${serviceStatus}</span>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="d-flex justify-content-between">
                        <span>数据库:</span>
                        <span class="badge ${databaseBadgeClass}">${databaseStatus}</span>
                    </div>
                </div>
                <div class="col-md-6 mt-2">
                    <div class="d-flex justify-content-between">
                        <span>版本:</span>
                        <span class="badge bg-info">${data.version || '-'}</span>
                    </div>
                </div>
                <div class="col-md-6 mt-2">
                    <div class="d-flex justify-content-between">
                        <span>运行时间:</span>
                        <span class="badge bg-secondary">${formatUptime(uptimeSource)}</span>
                    </div>
                </div>
            </div>
        `;

        document.getElementById('system-status').innerHTML = statusHtml;
    } catch (error) {
        console.error('加载系统状态失败:', error);
        document.getElementById('system-status').innerHTML = '<div class="alert alert-danger">加载系统状态失败</div>';
    }
}

// 加载最近活动
async function loadRecentActivity() {
    try {
        const container = document.getElementById('recent-activity');

        // 显示加载状态
        container.innerHTML = `
            <div class="loading text-center">
                <div class="spinner-border" role="status">
                    <span class="visually-hidden">加载中...</span>
                </div>
            </div>
        `;

        const response = await fetch('/api/admin/recent_activity?limit=8', {
            credentials: 'include'
        });

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }

        const data = await response.json();

        if (!data.success) {
            throw new Error(data.message || '获取最近活动失败');
        }

        const activities = data.activities || [];

        if (activities.length === 0) {
            container.innerHTML = '<div class="text-center text-muted">暂无最近活动</div>';
            return;
        }

        const activityHtml = `
            <div class="list-group list-group-flush">
                ${activities.map(activity => {
                    const timeAgo = getTimeAgo(activity.timestamp);
                    const colorClass = `bg-${activity.color}`;

                    return `
                        <div class="list-group-item d-flex justify-content-between align-items-start">
                            <div class="me-auto">
                                <div class="d-flex align-items-center mb-1">
                                    <i class="bi ${activity.icon} me-2 text-${activity.color}"></i>
                                    <div class="fw-bold">${activity.title}</div>
                                </div>
                                <small class="text-muted">${activity.description}</small>
                                <br>
                                <small class="text-muted">${timeAgo}</small>
                            </div>
                            <span class="badge ${colorClass} rounded-pill">
                                <i class="bi ${activity.icon}"></i>
                            </span>
                        </div>
                    `;
                }).join('')}
            </div>
        `;

        container.innerHTML = activityHtml;
        console.log(`已加载 ${activities.length} 条最近活动`);

    } catch (error) {
        console.error('加载最近活动失败:', error);
        document.getElementById('recent-activity').innerHTML =
            `<div class="text-center text-danger">
                <i class="bi bi-exclamation-triangle"></i>
                加载最近活动失败: ${error.message}
            </div>`;
    }
}

// 加载许可证列表
async function loadLicenses() {
    try {
        const response = await fetch('/api/admin/licenses', {
            credentials: 'include',
            cache: 'no-cache'
        });
        const data = await response.json();
        
        if (data.success) {
            const tableBody = document.getElementById('licenses-table');
            const topLevelLicenses = (data.licenses || []).filter(license => !license.parent_license_id);
            if (topLevelLicenses.length === 0) {
                tableBody.innerHTML = '<tr><td colspan="7" class="text-center text-muted">暂无许可证数据</td></tr>';
                return;
            }
            
            const rows = topLevelLicenses.map(license => `
                <tr>
                    <td>
                        <div class="license-key-display" title="点击复制许可证密钥" data-license-key="${license.key_string}" onclick="copyLicenseKey(this.dataset.licenseKey)">
                            ${license.key_string}
                        </div>
                    </td>
                    <td>
                        <span class="badge bg-primary">${getLicenseTypeText(license.key_type)}</span>
                    </td>
                    <td>
                        ${license.client_hardware_id ?
                            `<div class="hardware-id-display" title="点击查看完整硬件ID" data-hardware-id="${license.client_hardware_id}" onclick="showFullHardwareId(this.dataset.hardwareId)">
                                ${license.client_hardware_id}
                            </div>` :
                            '<span class="text-muted">未绑定</span>'
                        }
                    </td>
                    <td>${formatDateTime(license.created_at)}</td>
                    <td>${getExpireStatusBadge(license.expires_at)}</td>
                    <td>
                        <span class="badge ${license.is_active ? 'bg-success' : 'bg-danger'}">
                            ${license.is_active ? '活跃' : '禁用'}
                        </span>
                    </td>
                    <td>
                        <div class="btn-group" role="group">
                            <button class="btn btn-sm btn-outline-info" onclick="viewLicenseDetails('${license.id}')" title="详情">
                                <i class="bi bi-eye"></i>
                            </button>
                            <button class="btn btn-sm btn-outline-primary" onclick="editLicense('${license.id}')" title="编辑">
                                <i class="bi bi-pencil"></i>
                            </button>
                            <button class="btn btn-sm btn-outline-${license.is_active ? 'warning' : 'success'}"
                                    onclick="toggleLicense('${license.id}')"
                                    title="${license.is_active ? '禁用' : '启用'}">
                                <i class="bi bi-${license.is_active ? 'pause' : 'play'}"></i>
                            </button>
                            <button class="btn btn-sm btn-outline-secondary" data-license-key="${license.key_string}" onclick="copyLicenseKey(this.dataset.licenseKey)" title="复制密钥">
                                <i class="bi bi-clipboard"></i>
                            </button>
                            <button class="btn btn-sm btn-outline-danger" data-license-id="${license.id}" data-license-key="${license.key_string}" onclick="deleteLicense(this.dataset.licenseId, this.dataset.licenseKey)" title="删除">
                                <i class="bi bi-trash"></i>
                            </button>
                        </div>
                    </td>
                </tr>
            `).join('');
            
            tableBody.innerHTML = rows;
        } else {
            showAlert('加载许可证列表失败', 'danger');
        }
    } catch (error) {
        console.error('加载许可证列表失败:', error);
        showAlert('加载许可证列表失败', 'danger');
    }
}

// 切换有效期设置显示
function toggleExpireSettings() {
    const expireType = document.getElementById('licenseExpireType').value;
    const presetGroup = document.getElementById('presetExpireGroup');
    const customGroup = document.getElementById('customExpireGroup');

    presetGroup.style.display = expireType === 'preset' ? 'block' : 'none';
    customGroup.style.display = expireType === 'custom' ? 'block' : 'none';
}

// 切换创建许可证类型相关字段显示
function toggleCreateLicenseTypeFields() {
    const licenseTypeElement = document.getElementById('licenseType');
    const editorManagedLimitGroup = document.getElementById('editorManagedLimitGroup');
    const executorParentKeyGroup = document.getElementById('executorParentKeyGroup');
    const executorCreateCountGroup = document.getElementById('executorCreateCountGroup');

    if (!licenseTypeElement || !editorManagedLimitGroup || !executorParentKeyGroup || !executorCreateCountGroup) {
        return;
    }

    const licenseType = String(licenseTypeElement.value || '').toUpperCase();
    const isEditor = licenseType === 'EDITOR';

    editorManagedLimitGroup.style.display = isEditor ? 'block' : 'none';
    executorParentKeyGroup.style.display = isEditor ? 'none' : 'block';
    executorCreateCountGroup.style.display = isEditor ? 'none' : 'block';
}

// 切换编辑有效期设置显示
function toggleEditExpireSettings() {
    const expireType = document.getElementById('editExpireType').value;
    const customDateGroup = document.getElementById('editCustomDateGroup');
    const extendGroup = document.getElementById('editExtendGroup');

    customDateGroup.style.display = expireType === 'custom_date' ? 'block' : 'none';
    extendGroup.style.display = expireType === 'extend' ? 'block' : 'none';
}

// 切换编辑许可证类型相关字段显示
function toggleEditLicenseTypeFields(licenseTypeValue) {
    const maxActivationsLabel = document.getElementById('editMaxActivationsLabel');
    const maxActivationsInput = document.getElementById('editMaxActivations');
    const parentKeyGroup = document.getElementById('editExecutorParentKeyGroup');
    const parentKeyInput = document.getElementById('editExecutorParentLicenseKey');

    if (!maxActivationsLabel || !maxActivationsInput || !parentKeyGroup || !parentKeyInput) {
        return;
    }

    const licenseType = String(licenseTypeValue || '').toUpperCase();
    if (licenseType === 'EDITOR') {
        maxActivationsLabel.textContent = '可管理执行器数量';
        maxActivationsInput.min = '0';
        parentKeyGroup.style.display = 'none';
        parentKeyInput.value = '';
        return;
    }

    maxActivationsLabel.textContent = '最大激活数量';
    maxActivationsInput.min = '1';
    parentKeyGroup.style.display = licenseType === 'EXECUTOR' ? 'block' : 'none';
    if (licenseType !== 'EXECUTOR') {
        parentKeyInput.value = '';
    }
}

// 计算过期天数
function calculateExpireDays() {
    const expireType = document.getElementById('licenseExpireType').value;

    if (expireType === 'permanent') {
        return null; // 永久有效
    } else if (expireType === 'preset') {
        return parseInt(document.getElementById('presetExpire').value);
    } else if (expireType === 'custom') {
        const value = parseInt(document.getElementById('customExpireValue').value);
        const unit = document.getElementById('customExpireUnit').value;

        if (!value || value <= 0) {
            return null;
        }

        switch (unit) {
            case 'days':
                return value;
            case 'weeks':
                return value * 7;
            case 'months':
                return value * 30; // 近似值
            case 'years':
                return value * 365; // 近似值
            default:
                return value;
        }
    }

    return null;
}

// 创建许可证
async function createLicense() {
    const form = document.getElementById('createLicenseForm');
    const licenseType = String(document.getElementById('licenseType').value || '').toUpperCase();

    const licenseData = {
        key_type: licenseType,
        expires_days: calculateExpireDays()
    };

    if (licenseType === 'EDITOR') {
        const managedLimitRaw = document.getElementById('editorManagedLimit').value;
        const managedLimit = parseInt(managedLimitRaw, 10);
        if (Number.isNaN(managedLimit) || managedLimit < 0) {
            showAlert('编辑器可管理执行器数量必须为非负整数', 'warning');
            return;
        }
        licenseData.managed_executor_limit = managedLimit;
    } else if (licenseType === 'EXECUTOR') {
        const parentLicenseKey = document.getElementById('executorParentLicenseKey').value.trim();
        const createCountRaw = document.getElementById('executorCreateCount').value;
        const createCount = parseInt(createCountRaw, 10);
        if (!parentLicenseKey) {
            showAlert('创建执行器授权码时必须填写上级编辑器授权码', 'warning');
            return;
        }
        if (Number.isNaN(createCount) || createCount < 1) {
            showAlert('批量创建数量必须为大于等于1的整数', 'warning');
            return;
        }
        licenseData.parent_license_key = parentLicenseKey;
        licenseData.create_count = createCount;
    }
    
    try {
        const response = await fetch('/api/licensing/create_license', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(licenseData)
        });
        
        const data = await response.json();
        
        if (response.ok && data.success) {
            const createdCount = parseInt(data.created_count || 1, 10);
            const createdKeys = Array.isArray(data.created_license_keys) ? data.created_license_keys : [];
            if (createdCount > 1) {
                const preview = createdKeys.length > 0 ? `，首个授权码: ${createdKeys[0]}` : '';
                showAlert(`批量创建成功，共 ${createdCount} 个执行器授权码${preview}`, 'success');
            } else {
                showAlert(`许可证创建成功: ${data.license_key}`, 'success');
            }
            bootstrap.Modal.getInstance(document.getElementById('createLicenseModal')).hide();
            form.reset();
            toggleExpireSettings();
            toggleCreateLicenseTypeFields();
            if (currentSection === 'licenses') {
                loadLicenses();
            }
        } else {
            showAlert(data.detail || data.message || '创建许可证失败', 'danger');
        }
    } catch (error) {
        console.error('创建许可证失败:', error);
        showAlert(error.message || '创建许可证失败', 'danger');
    }
}

// 切换许可证状态
async function toggleLicense(licenseId) {
    try {
        const response = await fetch(`/api/admin/license/${licenseId}/toggle`, {
            method: 'POST',
            credentials: 'include'
        });

        const data = await response.json();

        if (response.ok && data.success) {
            showAlert(data.message || '许可证状态切换成功', 'success');
            loadLicenses();
        } else {
            throw new Error(data.detail || data.message || '操作失败');
        }
    } catch (error) {
        console.error('切换许可证状态失败:', error);
        showAlert('切换许可证状态失败: ' + error.message, 'danger');
    }
}

// 刷新函数
function refreshDashboard() {
    loadDashboard();
}

function refreshLicenses() {
    loadLicenses();
}

function refreshClients() {
    loadClients();
}

// 客户端状态过滤功能
function filterClientsByStatus(status) {
    const tableBody = document.getElementById('clients-table');
    if (!tableBody) return;

    const rows = tableBody.querySelectorAll('tr');
    let visibleCount = 0;
    let totalOnline = 0;
    let totalOffline = 0;

    rows.forEach(row => {
        // 跳过空状态行
        if (row.querySelector('td[colspan]')) {
            return;
        }

        // 获取状态徽章
        const statusBadge = row.querySelector('td:nth-child(5) .badge');
        if (!statusBadge) return;

        const isOnline = statusBadge.textContent.trim() === '在线';

        // 统计在线和离线数量
        if (isOnline) {
            totalOnline++;
        } else {
            totalOffline++;
        }

        // 根据过滤条件显示/隐藏行
        switch(status) {
            case 'all':
                row.style.display = '';
                visibleCount++;
                break;
            case 'online':
                if (isOnline) {
                    row.style.display = '';
                    visibleCount++;
                } else {
                    row.style.display = 'none';
                }
                break;
            case 'offline':
                if (!isOnline) {
                    row.style.display = '';
                    visibleCount++;
                } else {
                    row.style.display = 'none';
                }
                break;
        }
    });

    // 更新统计信息
    const totalClients = totalOnline + totalOffline;
    updateClientsStats(totalClients, totalOnline, totalOffline);

    // 如果没有可见的行，显示提示信息
    if (visibleCount === 0) {
        const emptyRow = document.createElement('tr');
        emptyRow.className = 'client-filter-empty';
        emptyRow.innerHTML = '<td colspan="7" class="text-center text-muted py-4"><i class="bi bi-info-circle me-2"></i>没有符合条件的客户端</td>';

        // 移除旧的空提示行
        const oldEmpty = tableBody.querySelector('.client-filter-empty');
        if (oldEmpty) oldEmpty.remove();

        tableBody.appendChild(emptyRow);
    } else {
        // 移除空提示行
        const emptyRow = tableBody.querySelector('.client-filter-empty');
        if (emptyRow) emptyRow.remove();
    }

    // 更新按钮状态反馈
    console.log(`过滤完成: ${status}, 可见行数: ${visibleCount}, 在线: ${totalOnline}, 离线: ${totalOffline}`);
}

// 更新客户端统计信息
function updateClientsStats(total, online, offline) {
    const statsBar = document.getElementById('clientsStatsBar');
    const totalEl = document.getElementById('clientsTotal');
    const onlineEl = document.getElementById('clientsOnline');
    const offlineEl = document.getElementById('clientsOffline');

    if (statsBar && totalEl && onlineEl && offlineEl) {
        // 显示统计栏
        statsBar.style.display = 'block';

        // 更新数值
        totalEl.textContent = total;
        onlineEl.textContent = online;
        offlineEl.textContent = offline;
    }
}

function refreshBannedList() {
    loadBannedList();
}

// 显示封禁列表
function showBannedClients() {
    const bannedSection = document.getElementById('banned-list-section');
    if (bannedSection) {
        bannedSection.style.display = 'block';
        loadBannedList();

        // 滚动到封禁列表
        bannedSection.scrollIntoView({ behavior: 'smooth' });
    }
}

// 隐藏封禁列表
function hideBannedList() {
    const bannedSection = document.getElementById('banned-list-section');
    if (bannedSection) {
        bannedSection.style.display = 'none';
    }
}

function refreshUsers() {
    loadUsers();
}

function refreshLogs() {
    loadLogs();
}

// 创建用户
function refreshMarketPackages() {
    loadMarketPackages();
}

function formatMarketFileSize(fileSize) {
    const size = Number(fileSize) || 0;
    if (size <= 0) {
        return '-';
    }
    if (size < 1024) {
        return `${size} B`;
    }
    if (size < 1024 * 1024) {
        return `${(size / 1024).toFixed(1)} KB`;
    }
    if (size < 1024 * 1024 * 1024) {
        return `${(size / 1024 / 1024).toFixed(1)} MB`;
    }
    return `${(size / 1024 / 1024 / 1024).toFixed(1)} GB`;
}

function getMarketStatusBadge(status) {
    const normalized = String(status || '').trim().toLowerCase();
    if (normalized === 'released') {
        return '<span class="badge bg-success">已发布</span>';
    }
    if (normalized === 'submitted') {
        return '<span class="badge bg-warning text-dark">待审核</span>';
    }
    if (normalized === 'rejected') {
        return '<span class="badge bg-danger">已拒绝</span>';
    }
    if (normalized === 'draft') {
        return '<span class="badge bg-secondary">草稿</span>';
    }
    return `<span class="badge bg-secondary">${escapeHtml(normalized || '-')}</span>`;
}

function buildMarketActionButtons(item) {
    const packageId = escapeHtml(String(item.package_id || ''));
    const version = escapeHtml(String(item.version || ''));
    const normalizedStatus = String(item.status || '').trim().toLowerCase();
    const buttons = [
        `
            <button type="button" class="btn btn-sm btn-outline-primary"
                    data-package-id="${packageId}"
                    data-version="${version}"
                    onclick="viewMarketPackageDetailsByElement(this)">
                详情
            </button>
        `,
    ];

    if (normalizedStatus !== 'released') {
        buttons.push(`
            <button type="button" class="btn btn-sm btn-success"
                    data-package-id="${packageId}"
                    data-version="${version}"
                    data-action="released"
                    onclick="reviewMarketPackageByElement(this)">
                发布
            </button>
        `);
    }
    if (normalizedStatus !== 'rejected') {
        buttons.push(`
            <button type="button" class="btn btn-sm btn-outline-danger"
                    data-package-id="${packageId}"
                    data-version="${version}"
                    data-action="rejected"
                    onclick="reviewMarketPackageByElement(this)">
                驳回
            </button>
        `);
    }
    if (normalizedStatus !== 'released') {
        buttons.push(`
            <button type="button" class="btn btn-sm btn-danger"
                    data-package-id="${packageId}"
                    data-version="${version}"
                    onclick="deleteMarketPackageByElement(this)">
                删除
            </button>
        `);
    }

    return `<div class="btn-group btn-group-sm" role="group">${buttons.join('')}</div>`;
}

function renderMarketPackages(items) {
    const container = document.getElementById('market-packages-container');
    const summaryElement = document.getElementById('market-summary-text');
    if (!container) {
        return;
    }

    const rows = Array.isArray(items) ? items : [];
    const submittedCount = rows.filter(item => String(item.status || '').trim().toLowerCase() === 'submitted').length;
    const releasedCount = rows.filter(item => String(item.status || '').trim().toLowerCase() === 'released').length;
    const rejectedCount = rows.filter(item => String(item.status || '').trim().toLowerCase() === 'rejected').length;

    if (summaryElement) {
        summaryElement.textContent = `共 ${rows.length} 个版本，待审核 ${submittedCount}，已发布 ${releasedCount}，已拒绝 ${rejectedCount}`;
    }

    if (!rows.length) {
        container.innerHTML = `
            <tr>
                <td colspan="7" class="text-center text-muted">暂无共享平台包数据</td>
            </tr>
        `;
        return;
    }

    container.innerHTML = rows.map(item => {
        const title = escapeHtml(String(item.title || item.package_id || '-'));
        const packageId = escapeHtml(String(item.package_id || '-'));
        const category = escapeHtml(String(item.category || ''));
        const summary = escapeHtml(String(item.summary || ''));
        const version = escapeHtml(String(item.version || '-'));
        const latestVersion = escapeHtml(String(item.latest_version || '-'));
        const reviewComment = escapeHtml(String(item.review_comment || ''));
        const storagePath = escapeHtml(String(item.storage_path || ''));
        const fileSha256 = escapeHtml(String(item.file_sha256 || ''));
        const downloadUrl = String(item.download_url || '').trim();
        const summaryHtml = summary ? `<div class="small text-muted text-break mt-1">${summary}</div>` : '';
        const categoryHtml = category ? `<div class="small mt-1"><span class="badge bg-light text-dark border">${category}</span></div>` : '';
        const reviewHtml = reviewComment ? `<div class="small text-muted text-break mt-1">${reviewComment}</div>` : '';
        const storageHtml = storagePath ? `<div class="small text-muted text-break">${storagePath}</div>` : '';
        const shaHtml = fileSha256 ? `<div class="small text-muted">SHA256: ${fileSha256.slice(0, 16)}...</div>` : '';
        const downloadHtml = downloadUrl
            ? `<a class="btn btn-sm btn-outline-primary" href="${escapeHtml(downloadUrl)}" target="_blank" rel="noopener noreferrer">下载</a>`
            : '<span class="text-muted">-</span>';

        return `
            <tr>
                <td>
                    <div class="fw-semibold">${title}</div>
                    <div class="small text-muted text-break">${packageId}</div>
                    ${categoryHtml}
                    ${summaryHtml}
                </td>
                <td>
                    <div>${version}</div>
                    <div class="small text-muted">当前发布: ${latestVersion}</div>
                </td>
                <td>
                    ${getMarketStatusBadge(item.status)}
                    ${reviewHtml}
                </td>
                <td>
                    <div>${formatMarketFileSize(item.file_size)}</div>
                    ${shaHtml}
                    ${storageHtml}
                </td>
                <td>
                    <div class="small">提交: ${formatDateTime(item.created_at)}</div>
                    <div class="small text-muted">审核: ${formatDateTime(item.reviewed_at)}</div>
                    <div class="small text-muted">发布: ${formatDateTime(item.published_at)}</div>
                </td>
                <td>${downloadHtml}</td>
                <td>${buildMarketActionButtons(item)}</td>
            </tr>
        `;
    }).join('');
}

function copyMarketDetailValueByElement(element) {
    if (!element) {
        return;
    }
    const value = String(element.dataset.copyText || '').trim();
    if (!value) {
        showAlert('没有可复制的内容', 'warning');
        return;
    }
    copyToClipboard(value);
}

function buildMarketReviewHistoryRows(reviewHistory) {
    const rows = Array.isArray(reviewHistory) ? reviewHistory : [];
    if (!rows.length) {
        return `
            <tr>
                <td colspan="4" class="text-center text-muted">暂无审核历史</td>
            </tr>
        `;
    }

    return rows.map(item => {
        const reviewer = escapeHtml(String(item.reviewer || '-'));
        const comment = String(item.comment || '').trim();
        return `
            <tr>
                <td>${reviewer}</td>
                <td>${getMarketStatusBadge(item.action)}</td>
                <td>${comment ? `<div class="text-break">${escapeHtml(comment)}</div>` : '<span class="text-muted">-</span>'}</td>
                <td>${formatDateTime(item.created_at)}</td>
            </tr>
        `;
    }).join('');
}

function bindMarketPackageDetailsModal() {
    const modalElement = document.getElementById('marketPackageDetailsModal');
    if (!modalElement || modalElement.dataset.marketBound === '1') {
        return modalElement;
    }
    modalElement.addEventListener('hidden.bs.modal', function () {
        window.marketPackageDetailContext = null;
    });
    modalElement.dataset.marketBound = '1';
    return modalElement;
}

function viewMarketPackageDetailsByElement(element) {
    if (!element) {
        return;
    }
    const packageId = String(element.dataset.packageId || '').trim();
    const version = String(element.dataset.version || '').trim();
    viewMarketPackageDetails(packageId, version);
}

async function viewMarketPackageDetails(packageId, version) {
    if (!packageId || !version) {
        showAlert('共享平台包参数不完整', 'warning');
        return;
    }

    try {
        const response = await fetch(`/api/market/admin/packages/${encodeURIComponent(packageId)}/${encodeURIComponent(version)}`, {
            credentials: 'include',
            cache: 'no-cache',
        });

        if (response.status === 401) {
            window.location.href = '/login';
            return;
        }

        let data = {};
        try {
            data = await response.json();
        } catch (_) {
            data = {};
        }

        if (!response.ok || !data.success || !data.package) {
            throw new Error(data.detail || data.message || '加载共享平台包详情失败');
        }

        const packageData = data.package || {};
        window.marketPackageDetailContext = {
            packageId: String(packageData.package_id || packageId),
            version: String(packageData.version || version),
        };

        const modalElement = bindMarketPackageDetailsModal();
        const contentElement = document.getElementById('marketPackageDetailsContent');
        if (!modalElement || !contentElement) {
            throw new Error('共享平台包详情弹窗未初始化');
        }

        const safeTitle = escapeHtml(String(packageData.title || packageData.package_id || '-'));
        const safePackageId = escapeHtml(String(packageData.package_id || '-'));
        const safeVersion = escapeHtml(String(packageData.version || '-'));
        const safeLatestVersion = escapeHtml(String(packageData.latest_version || '-'));
        const safeCategory = escapeHtml(String(packageData.category || '-'));
        const safeSummary = escapeHtml(String(packageData.summary || '').trim() || '-');
        const safeVisibility = escapeHtml(String(packageData.visibility || '-'));
        const safeReviewComment = escapeHtml(String(packageData.review_comment || '').trim() || '-');
        const safeStoragePath = escapeHtml(String(packageData.storage_path || '').trim() || '-');
        const safeFileSha256 = escapeHtml(String(packageData.file_sha256 || '').trim() || '-');
        const safeDownloadUrl = String(packageData.download_url || '').trim();
        const manifestText = escapeHtml(JSON.stringify(packageData.manifest || {}, null, 2));
        const changelogText = escapeHtml(String(packageData.changelog || '').trim() || '-');
        const releaseNotesText = escapeHtml(String(packageData.release_notes || '').trim() || '-');
        const historyRowsHtml = buildMarketReviewHistoryRows(packageData.review_history);
        const safeButtonPackageId = escapeHtml(String(packageData.package_id || packageId));
        const safeButtonVersion = escapeHtml(String(packageData.version || version));
        const normalizedStatus = String(packageData.status || '').trim().toLowerCase();

        const actionButtons = [];
        if (safeDownloadUrl) {
            actionButtons.push(`
                <a class="btn btn-sm btn-outline-primary" href="${escapeHtml(safeDownloadUrl)}" target="_blank" rel="noopener noreferrer">下载包</a>
            `);
            actionButtons.push(`
                <button type="button" class="btn btn-sm btn-outline-secondary" data-copy-text="${escapeHtml(safeDownloadUrl)}" onclick="copyMarketDetailValueByElement(this)">复制下载地址</button>
            `);
        }
        if (String(packageData.storage_path || '').trim()) {
            actionButtons.push(`
                <button type="button" class="btn btn-sm btn-outline-secondary" data-copy-text="${escapeHtml(String(packageData.storage_path || '').trim())}" onclick="copyMarketDetailValueByElement(this)">复制存储路径</button>
            `);
        }
        if (normalizedStatus !== 'released') {
            actionButtons.push(`
                <button type="button" class="btn btn-sm btn-success" data-package-id="${safeButtonPackageId}" data-version="${safeButtonVersion}" data-action="released" onclick="reviewMarketPackageByElement(this)">发布当前版本</button>
            `);
        }
        if (normalizedStatus !== 'rejected') {
            actionButtons.push(`
                <button type="button" class="btn btn-sm btn-outline-danger" data-package-id="${safeButtonPackageId}" data-version="${safeButtonVersion}" data-action="rejected" onclick="reviewMarketPackageByElement(this)">驳回当前版本</button>
            `);
        }
        if (normalizedStatus !== 'released') {
            actionButtons.push(`
                <button type="button" class="btn btn-sm btn-danger" data-package-id="${safeButtonPackageId}" data-version="${safeButtonVersion}" onclick="deleteMarketPackageByElement(this)">删除当前版本</button>
            `);
        }

        contentElement.innerHTML = `
            <div class="row g-3">
                <div class="col-lg-6">
                    <div class="card h-100">
                        <div class="card-header"><strong>基础信息</strong></div>
                        <div class="card-body">
                            <table class="table table-borderless table-sm mb-0">
                                <tr><th style="width: 9rem;">标题</th><td>${safeTitle}</td></tr>
                                <tr><th>Package ID</th><td><code>${safePackageId}</code></td></tr>
                                <tr><th>版本</th><td>${safeVersion}</td></tr>
                                <tr><th>当前发布</th><td>${safeLatestVersion}</td></tr>
                                <tr><th>分类</th><td>${safeCategory}</td></tr>
                                <tr><th>可见性</th><td>${safeVisibility}</td></tr>
                                <tr><th>状态</th><td>${getMarketStatusBadge(packageData.status)}</td></tr>
                                <tr><th>摘要</th><td class="text-break">${safeSummary}</td></tr>
                                <tr><th>审核备注</th><td class="text-break">${safeReviewComment}</td></tr>
                            </table>
                        </div>
                    </div>
                </div>
                <div class="col-lg-6">
                    <div class="card h-100">
                        <div class="card-header"><strong>文件与时间</strong></div>
                        <div class="card-body">
                            <table class="table table-borderless table-sm mb-0">
                                <tr><th style="width: 9rem;">文件大小</th><td>${formatMarketFileSize(packageData.file_size)}</td></tr>
                                <tr><th>SHA256</th><td class="text-break"><code>${safeFileSha256}</code></td></tr>
                                <tr><th>存储路径</th><td class="text-break">${safeStoragePath}</td></tr>
                                <tr><th>提交时间</th><td>${formatDateTime(packageData.created_at)}</td></tr>
                                <tr><th>审核时间</th><td>${formatDateTime(packageData.reviewed_at)}</td></tr>
                                <tr><th>发布时间</th><td>${formatDateTime(packageData.published_at)}</td></tr>
                            </table>
                            <div class="mt-3 d-flex flex-wrap gap-2">
                                ${actionButtons.join('')}
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-12">
                    <div class="card">
                        <div class="card-header"><strong>Manifest</strong></div>
                        <div class="card-body">
                            <pre class="bg-light border rounded p-3 small mb-0" style="white-space: pre-wrap; word-break: break-word; max-height: 320px; overflow: auto;">${manifestText}</pre>
                        </div>
                    </div>
                </div>
                <div class="col-lg-6">
                    <div class="card h-100">
                        <div class="card-header"><strong>变更说明</strong></div>
                        <div class="card-body">
                            <pre class="bg-light border rounded p-3 small mb-0" style="white-space: pre-wrap; word-break: break-word; max-height: 240px; overflow: auto;">${changelogText}</pre>
                        </div>
                    </div>
                </div>
                <div class="col-lg-6">
                    <div class="card h-100">
                        <div class="card-header"><strong>发布备注</strong></div>
                        <div class="card-body">
                            <pre class="bg-light border rounded p-3 small mb-0" style="white-space: pre-wrap; word-break: break-word; max-height: 240px; overflow: auto;">${releaseNotesText}</pre>
                        </div>
                    </div>
                </div>
                <div class="col-12">
                    <div class="card">
                        <div class="card-header"><strong>审核历史</strong></div>
                        <div class="card-body">
                            <div class="table-responsive">
                                <table class="table table-hover align-middle mb-0">
                                    <thead>
                                        <tr>
                                            <th>审核人</th>
                                            <th>操作</th>
                                            <th>说明</th>
                                            <th>时间</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        ${historyRowsHtml}
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;

        const modal = new bootstrap.Modal(modalElement);
        modal.show();
    } catch (error) {
        console.error('加载共享平台包详情失败:', error);
        showAlert(error.message || '加载共享平台包详情失败', 'danger');
    }
}

async function loadMarketPackages() {
    const container = document.getElementById('market-packages-container');
    const summaryElement = document.getElementById('market-summary-text');
    if (!container) {
        return;
    }

    showLoading('market-packages-container');
    if (summaryElement) {
        summaryElement.textContent = '加载中...';
    }

    try {
        const statusFilterElement = document.getElementById('marketStatusFilter');
        const statusValue = statusFilterElement ? String(statusFilterElement.value || '').trim() : '';
        const query = statusValue ? `?status=${encodeURIComponent(statusValue)}` : '';
        const response = await fetch(`/api/market/admin/packages${query}`, {
            credentials: 'include',
            cache: 'no-cache',
        });

        if (response.status === 401) {
            window.location.href = '/login';
            return;
        }

        let data = {};
        try {
            data = await response.json();
        } catch (_) {
            data = {};
        }

        if (!response.ok) {
            throw new Error(data.detail || data.message || '加载共享平台包失败');
        }

        renderMarketPackages(data.items || []);
    } catch (error) {
        console.error('加载共享平台包失败:', error);
        showError('market-packages-container', error.message || '加载共享平台包失败');
        if (summaryElement) {
            summaryElement.textContent = '加载失败';
        }
    }
}

function reviewMarketPackageByElement(element) {
    if (!element) {
        return;
    }
    const packageId = String(element.dataset.packageId || '').trim();
    const version = String(element.dataset.version || '').trim();
    const action = String(element.dataset.action || '').trim();
    reviewMarketPackage(packageId, version, action);
}

function deleteMarketPackageByElement(element) {
    if (!element) {
        return;
    }
    const packageId = String(element.dataset.packageId || '').trim();
    const version = String(element.dataset.version || '').trim();
    deleteMarketPackage(packageId, version);
}

async function deleteMarketPackage(packageId, version) {
    if (!packageId || !version) {
        showAlert('\u5e02\u573a\u5305\u53c2\u6570\u4e0d\u5b8c\u6574', 'warning');
        return;
    }

    const confirmed = window.confirm(`确认删除 ${packageId} @ ${version} 吗？

仅允许删除未发布版本，此操作不可撤销。`);
    if (!confirmed) {
        return;
    }

    try {
        const response = await fetch(`/api/market/admin/packages/${encodeURIComponent(packageId)}/${encodeURIComponent(version)}`, {
            method: 'DELETE',
            credentials: 'include',
            cache: 'no-cache',
        });

        if (response.status === 401) {
            window.location.href = '/login';
            return;
        }

        let data = {};
        try {
            data = await response.json();
        } catch (_) {
            data = {};
        }

        if (!response.ok || !data.success) {
            throw new Error(data.detail || data.message || '\u5220\u9664\u5e02\u573a\u5305\u5931\u8d25');
        }

        await loadMarketPackages();

        const detailContext = window.marketPackageDetailContext || {};
        if (
            String(detailContext.packageId || '') === packageId
            && String(detailContext.version || '') === version
        ) {
            const modalElement = document.getElementById('marketPackageDetailsModal');
            const modalInstance = modalElement ? bootstrap.Modal.getInstance(modalElement) : null;
            if (modalInstance) {
                modalInstance.hide();
            }
            window.marketPackageDetailContext = null;
        }

        showAlert('\u5e02\u573a\u5305\u5220\u9664\u6210\u529f', 'success');
    } catch (error) {
        console.error('\u5220\u9664\u5e02\u573a\u5305\u5931\u8d25', error);
        showAlert(error.message || '\u5220\u9664\u5e02\u573a\u5305\u5931\u8d25', 'danger');
    }
}

async function reviewMarketPackage(packageId, version, action) {
    const normalizedAction = String(action || '').trim().toLowerCase();
    if (!packageId || !version || !normalizedAction) {
        showAlert('共享平台包参数不完整', 'warning');
        return;
    }

    let comment = '';
    if (normalizedAction === 'released') {
        const confirmed = window.confirm(`确认发布 ${packageId} @ ${version} 吗？`);
        if (!confirmed) {
            return;
        }
        const input = window.prompt('审核备注（可留空）', '');
        if (input !== null) {
            comment = String(input || '').trim();
        }
    } else if (normalizedAction === 'rejected') {
        const input = window.prompt('驳回说明（可留空）', '');
        if (input === null) {
            return;
        }
        comment = String(input || '').trim();
        const confirmed = window.confirm(`确认驳回 ${packageId} @ ${version} 吗？`);
        if (!confirmed) {
            return;
        }
    }

    try {
        const response = await fetch('/api/market/admin/review', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            credentials: 'include',
            body: JSON.stringify({
                package_id: packageId,
                version: version,
                action: normalizedAction,
                comment: comment,
            }),
        });

        if (response.status === 401) {
            window.location.href = '/login';
            return;
        }

        let data = {};
        try {
            data = await response.json();
        } catch (_) {
            data = {};
        }

        if (!response.ok || !data.success) {
            throw new Error(data.detail || data.message || '共享平台包审核失败');
        }

        await loadMarketPackages();
        if (
            window.marketPackageDetailContext
            && String(window.marketPackageDetailContext.packageId || '') === packageId
            && String(window.marketPackageDetailContext.version || '') === version
        ) {
            await viewMarketPackageDetails(packageId, version);
        }
        showAlert('共享平台包审核成功', 'success');
    } catch (error) {
        console.error('共享平台包审核失败:', error);
        showAlert(error.message || '共享平台包审核失败', 'danger');
    }
}
async function createUser() {
    const form = document.getElementById('createUserForm');
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;
    const hardwareId = document.getElementById('userHardwareId').value;
    const isAdmin = document.getElementById('isAdmin').checked;

    // 验证输入
    if (!username || !password) {
        showAlert('请填写用户名和密码', 'warning');
        return;
    }

    if (password !== confirmPassword) {
        showAlert('两次输入的密码不一致', 'warning');
        return;
    }

    if (hardwareId && hardwareId.length !== 64) {
        showAlert('硬件ID必须是64字符的SHA256值', 'warning');
        return;
    }

    try {
        // 这里应该调用实际的API
        showAlert(`用户 ${username} 创建成功`, 'success');
        bootstrap.Modal.getInstance(document.getElementById('createUserModal')).hide();
        form.reset();
        loadUsers();
    } catch (error) {
        console.error('创建用户失败:', error);
        showAlert('创建用户失败', 'danger');
    }
}

// 保存设置
async function saveSettings() {
    try {
        const serverName = String(document.getElementById('serverName').value || '').trim();
        if (!serverName) {
            showAlert('服务器名称不能为空', 'warning');
            return;
        }

        const marketUpdateServerBase = String(document.getElementById('marketUpdateServerBase').value || '').trim();
        if (marketUpdateServerBase.length > 500) {
            throw new Error('共享平台更新服务器地址长度不能超过500');
        }

        const parseIntField = (elementId, fieldLabel, minValue, maxValue) => {
            const raw = document.getElementById(elementId).value;
            const value = Number(raw);
            if (!Number.isInteger(value)) {
                throw new Error(`${fieldLabel}必须为整数`);
            }
            if (value < minValue || value > maxValue) {
                throw new Error(`${fieldLabel}必须在${minValue}到${maxValue}之间`);
            }
            return value;
        };

        const payload = {
            serverName: serverName,
            maxClients: parseIntField('maxClients', '最大客户端数量', 1, 1000000),
            sessionTimeout: parseIntField('sessionTimeout', '会话超时', 5, 1440),
            marketUpdateServerBase: marketUpdateServerBase,
            enableLogging: document.getElementById('enableLogging').checked,
            maxLoginAttempts: parseIntField('maxLoginAttempts', '最大登录尝试次数', 1, 20),
            lockoutDuration: parseIntField('lockoutDuration', '锁定时长', 1, 1440),
            enableCSRF: document.getElementById('enableCSRF').checked,
            enableRateLimit: document.getElementById('enableRateLimit').checked
        };

        const response = await fetch('/api/admin/settings', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            credentials: 'include',
            body: JSON.stringify(payload)
        });

        const data = await response.json();

        if (!response.ok || !data.success) {
            throw new Error(data.detail || data.message || '设置保存失败');
        }

        const settings = data.settings || payload;
        document.getElementById('serverName').value = settings.serverName ?? payload.serverName;
        document.getElementById('maxClients').value = settings.maxClients ?? payload.maxClients;
        document.getElementById('sessionTimeout').value = settings.sessionTimeout ?? payload.sessionTimeout;
        document.getElementById('marketUpdateServerBase').value = settings.marketUpdateServerBase ?? payload.marketUpdateServerBase ?? '';
        document.getElementById('enableLogging').checked = Boolean(settings.enableLogging);
        document.getElementById('maxLoginAttempts').value = settings.maxLoginAttempts ?? payload.maxLoginAttempts;
        document.getElementById('lockoutDuration').value = settings.lockoutDuration ?? payload.lockoutDuration;
        document.getElementById('enableCSRF').checked = Boolean(settings.enableCSRF);
        document.getElementById('enableRateLimit').checked = Boolean(settings.enableRateLimit);

        showAlert(data.message || '设置保存成功', 'success');
    } catch (error) {
        console.error('保存设置失败:', error);
        showAlert(error.message || '保存设置失败', 'danger');
    }
}

// 过滤日志
function filterLogs() {
    const level = document.getElementById('logLevel').value;
    console.log('过滤日志级别:', level);
    loadLogs(); // 重新加载日志，会应用过滤器
}

async function requestSecondaryPasswordForDelete(actionName) {
    const input = prompt(`${actionName}需要输入二级密码:`);
    if (input === null) {
        return null;
    }
    const secondaryPassword = String(input || '').trim();
    if (!secondaryPassword) {
        showAlert('二级密码不能为空', 'warning');
        return null;
    }
    return secondaryPassword;
}

async function sendDeleteRequestWithSecondaryVerification(url, actionName) {
    const buildDeleteOptions = (secondaryPassword) => {
        if (!secondaryPassword) {
            return {
                method: 'DELETE',
                credentials: 'include'
            };
        }
        return {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
            },
            credentials: 'include',
            body: JSON.stringify({
                secondary_password: secondaryPassword
            })
        };
    };

    let response = await fetch(url, buildDeleteOptions(null));
    let data = {};
    try {
        data = await response.json();
    } catch (_) {
        data = {};
    }

    if (response.status === 403) {
        const secondaryPassword = await requestSecondaryPasswordForDelete(actionName);
        if (!secondaryPassword) {
            return { cancelled: true, response, data };
        }
        response = await fetch(url, buildDeleteOptions(secondaryPassword));
        try {
            data = await response.json();
        } catch (_) {
            data = {};
        }
    }

    return { cancelled: false, response, data };
}

// 清空日志
async function clearLogs() {
    if (!confirm('确定要清空所有系统日志吗？此操作不可撤销！')) {
        return;
    }

    try {
        const result = await sendDeleteRequestWithSecondaryVerification('/api/admin/logs', '清空日志');
        if (result.cancelled) {
            return;
        }
        const { response, data } = result;

        if (response.ok && data.success) {
            showAlert(data.message || '日志已清空', 'success');
            // 重新加载日志显示
            loadLogs();
        } else {
            throw new Error(data.detail || data.message || '清空日志失败');
        }

    } catch (error) {
        console.error('清空日志失败:', error);
        showAlert('清空日志失败: ' + error.message, 'danger');
    }
}

// 查看客户端详情
async function viewClientDetails(hardwareId) {
    try {
        // 同时获取客户端信息、许可证信息和封禁信息
        const [clientsResponse, licensesResponse, bannedResponse] = await Promise.all([
            fetch('/api/admin/clients', { credentials: 'include', cache: 'no-cache' }),
            fetch('/api/admin/licenses', { credentials: 'include', cache: 'no-cache' }),
            fetch('/api/admin/banned_hardware_ids', { credentials: 'include', cache: 'no-cache' })
        ]);

        const clientsData = await clientsResponse.json();
        const licensesData = await licensesResponse.json();
        const bannedData = await bannedResponse.json();

        // 查找对应的客户端
        const client = clientsData.success ?
            clientsData.clients.find(c => c.hardware_id === hardwareId) : null;

        if (!client) {
            showAlert('找不到对应的客户端信息', 'warning');
            return;
        }

        // 查找相关的许可证
        const relatedLicenses = licensesData.success ?
            licensesData.licenses.filter(l => l.client_hardware_id === hardwareId) : [];

        // 查找封禁信息
        const banInfo = bannedData.success ?
            bannedData.banned_hardware_ids.find(b => b.hardware_id === hardwareId && b.is_active) : null;

        // 计算在线状态
        const now = new Date();
        const lastSeen = client.last_seen ? new Date(client.last_seen) : null;
        const isOnline = lastSeen && (now - lastSeen) / (1000 * 60 * 60) <= 24;

        showClientDetailsModal(client, relatedLicenses, banInfo, isOnline);

    } catch (error) {
        console.error('获取客户端详情失败:', error);
        showAlert('获取客户端详情失败: ' + error.message, 'danger');
    }
}

// 显示客户端详情模态框
function showClientDetailsModal(client, licenses, banInfo, isOnline) {
    const modalHtml = `
        <div class="modal fade" id="clientDetailsModal" tabindex="-1">
            <div class="modal-dialog modal-lg">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title">
                            <i class="bi bi-pc-display"></i> 客户端详情
                        </h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                    </div>
                    <div class="modal-body">
                        <div class="row">
                            <!-- 基本信息 -->
                            <div class="col-md-6">
                                <h6 class="text-primary"><i class="bi bi-info-circle"></i> 基本信息</h6>
                                <table class="table table-borderless table-sm">
                                    <tr>
                                        <td><strong>硬件ID:</strong></td>
                                        <td>
                                            <div class="hardware-id-display" style="font-size: 0.8rem; padding: 2px 4px;">
                                                ${client.hardware_id}
                                            </div>
                                            <button class="btn btn-sm btn-outline-secondary mt-1" onclick="copyToClipboard('${client.hardware_id}')">
                                                <i class="bi bi-clipboard"></i> 复制
                                            </button>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td><strong>注册时间:</strong></td>
                                        <td>${formatDateTime(client.registration_date)}</td>
                                    </tr>
                                    <tr>
                                        <td><strong>最后活动:</strong></td>
                                        <td>
                                            ${client.last_seen ? formatDateTime(client.last_seen) : '<span class="text-muted">从未</span>'}
                                        </td>
                                    </tr>
                                    <tr>
                                        <td><strong>在线状态:</strong></td>
                                        <td>
                                            <span class="badge ${isOnline ? 'bg-success' : 'bg-secondary'}">
                                                <i class="bi bi-${isOnline ? 'wifi' : 'wifi-off'}"></i>
                                                ${isOnline ? '在线' : '离线'}
                                            </span>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td><strong>账户状态:</strong></td>
                                        <td>
                                            <span class="badge ${client.is_active ? 'bg-success' : 'bg-danger'}">
                                                <i class="bi bi-${client.is_active ? 'check-circle' : 'x-circle'}"></i>
                                                ${client.is_active ? '活跃' : '禁用'}
                                            </span>
                                        </td>
                                    </tr>
                                </table>
                            </div>

                            <!-- 封禁状态 -->
                            <div class="col-md-6">
                                <h6 class="text-warning"><i class="bi bi-shield-exclamation"></i> 封禁状态</h6>
                                ${banInfo ? `
                                    <div class="alert alert-danger">
                                        <h6><i class="bi bi-shield-x"></i> 已被封禁</h6>
                                        <table class="table table-borderless table-sm mb-0">
                                            <tr>
                                                <td><strong>封禁原因:</strong></td>
                                                <td>${banInfo.reason || '未知原因'}</td>
                                            </tr>
                                            <tr>
                                                <td><strong>封禁时间:</strong></td>
                                                <td>${formatDateTime(banInfo.banned_at)}</td>
                                            </tr>
                                            <tr>
                                                <td><strong>操作员:</strong></td>
                                                <td>${banInfo.banned_by || '未知'}</td>
                                            </tr>
                                            <tr>
                                                <td><strong>过期时间:</strong></td>
                                                <td>${banInfo.expires_at ? formatDateTime(banInfo.expires_at) : '<span class="text-danger">永久</span>'}</td>
                                            </tr>
                                            ${banInfo.notes ? `
                                            <tr>
                                                <td><strong>备注:</strong></td>
                                                <td>${banInfo.notes}</td>
                                            </tr>
                                            ` : ''}
                                        </table>
                                        <div class="mt-2">
                                            <button class="btn btn-sm btn-success" onclick="quickUnbanClient('${client.hardware_id}'); bootstrap.Modal.getInstance(document.getElementById('clientDetailsModal')).hide();">
                                                <i class="bi bi-shield-check"></i> 解除封禁
                                            </button>
                                        </div>
                                    </div>
                                ` : `
                                    <div class="alert alert-success">
                                        <h6><i class="bi bi-check-circle"></i> 状态正常</h6>
                                        <p class="mb-2">该客户端未被封禁，可以正常使用所有功能。</p>
                                        <button class="btn btn-sm btn-warning" onclick="quickBanClient('${client.hardware_id}'); bootstrap.Modal.getInstance(document.getElementById('clientDetailsModal')).hide();">
                                            <i class="bi bi-shield-x"></i> 封禁此客户端
                                        </button>
                                    </div>
                                `}
                            </div>
                        </div>

                        <!-- 许可证信息 -->
                        <div class="row mt-3">
                            <div class="col-12">
                                <h6 class="text-info"><i class="bi bi-key"></i> 许可证信息 (${licenses.length})</h6>
                                ${licenses.length > 0 ? `
                                    <div class="table-responsive">
                                        <table class="table table-sm table-hover">
                                            <thead>
                                                <tr>
                                                    <th>许可证密钥</th>
                                                    <th>类型</th>
                                                    <th>创建时间</th>
                                                    <th>过期时间</th>
                                                    <th>状态</th>
                                                    <th>操作</th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                ${licenses.map(license => `
                                                    <tr>
                                                        <td>
                                                            <div class="license-key-display" style="font-size: 0.75rem; padding: 2px 4px;">
                                                                ${license.key_string}
                                                            </div>
                                                        </td>
                                                        <td><span class="badge bg-primary">${getLicenseTypeText(license.key_type)}</span></td>
                                                        <td>${formatDateTime(license.created_at)}</td>
                                                        <td>${license.expires_at ? formatDateTime(license.expires_at) : '<span class="text-muted">永久</span>'}</td>
                                                        <td>
                                                            <span class="badge ${license.is_active ? 'bg-success' : 'bg-danger'}">
                                                                ${license.is_active ? '活跃' : '禁用'}
                                                            </span>
                                                        </td>
                                                        <td>
                                                            <button class="btn btn-sm btn-outline-secondary" onclick="copyToClipboard('${license.key_string}')" title="复制">
                                                                <i class="bi bi-clipboard"></i>
                                                            </button>
                                                        </td>
                                                    </tr>
                                                `).join('')}
                                            </tbody>
                                        </table>
                                    </div>
                                ` : `
                                    <div class="alert alert-info">
                                        <i class="bi bi-info-circle"></i> 该客户端暂无绑定的许可证
                                    </div>
                                `}
                            </div>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">关闭</button>
                        <button type="button" class="btn btn-danger" onclick="removeClient('${client.hardware_id}'); bootstrap.Modal.getInstance(document.getElementById('clientDetailsModal')).hide();">
                            <i class="bi bi-trash"></i> 移除客户端
                        </button>
                    </div>
                </div>
            </div>
        </div>
    `;

    // 移除现有模态框
    const existingModal = document.getElementById('clientDetailsModal');
    if (existingModal) {
        existingModal.remove();
    }

    // 添加新模态框
    document.body.insertAdjacentHTML('beforeend', modalHtml);

    // 显示模态框
    const modal = new bootstrap.Modal(document.getElementById('clientDetailsModal'));
    modal.show();

    // 模态框关闭时移除DOM元素
    modal._element.addEventListener('hidden.bs.modal', function () {
        this.remove();
    });
}

// 移除客户端
async function removeClient(hardwareId) {
    if (confirm(`确定要删除客户端 ${hardwareId} 吗？\n\n此操作将会：\n• 删除客户端记录\n• 删除所有相关许可证\n• 删除相关封禁记录\n\n此操作不可撤销！`)) {
        try {
            const result = await sendDeleteRequestWithSecondaryVerification(`/api/admin/client/${hardwareId}`, '删除客户端');
            if (result.cancelled) {
                return;
            }
            const { response, data } = result;

            if (response.ok && data.success) {
                showAlert('客户端删除成功', 'success');
                loadClients(); // 刷新客户端列表
            } else {
                throw new Error(data.detail || data.message || '删除失败');
            }
        } catch (error) {
            console.error('删除客户端失败:', error);
            showAlert('删除客户端失败: ' + error.message, 'danger');
        }
    }
}

// 编辑用户
function editUser(userId) {
    showAlert(`编辑用户: ${userId}`, 'info');
}

// 删除用户
function deleteUser(userId) {
    if (confirm('确定要删除这个用户吗？')) {
        showAlert(`用户已删除`, 'success');
        loadUsers();
    }
}

// 自动刷新
function startAutoRefresh() {
// auto refresh every 30 seconds
    refreshInterval = setInterval(() => {
        if (currentSection === 'dashboard') {
            loadDashboard();
        } else if (currentSection === 'market') {
            loadMarketPackages();
        }
    }, 30000);
}

// 工具函数
function parseApiDate(dateValue) {
    const raw = String(dateValue || '').trim();
    if (!raw) {
        return null;
    }
    const hasTimezone = /([zZ]|[+-]\d{2}:\d{2})$/.test(raw);
    const normalized = hasTimezone ? raw : `${raw}Z`;
    const parsed = new Date(normalized);
    if (Number.isNaN(parsed.getTime())) {
        return null;
    }
    return parsed;
}

function formatDurationFromSeconds(totalSeconds) {
    const seconds = Math.max(0, Math.floor(Number(totalSeconds) || 0));
    const days = Math.floor(seconds / 86400);
    const hours = Math.floor((seconds % 86400) / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    if (days > 0) {
        return `${days}天${hours}小时${minutes}分钟`;
    }
    return `${hours}小时${minutes}分钟`;
}

function formatDateTime(dateString) {
    const date = parseApiDate(dateString);
    if (!date) {
        return '-';
    }
    // 转换为北京时间显示
    return date.toLocaleString('zh-CN', {
        timeZone: 'Asia/Shanghai',
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
    });
}

// HTML转义函数
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// 显示加载状态
function showLoading(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
        element.innerHTML = `
            <tr>
                <td colspan="7" class="text-center">
                    <div class="loading">
                        <div class="spinner-border" role="status">
                            <span class="visually-hidden">加载中...</span>
                        </div>
                    </div>
                </td>
            </tr>
        `;
    }
}

// 显示错误信息
function showError(elementId, message) {
    const element = document.getElementById(elementId);
    if (element) {
        element.innerHTML = `
            <tr>
                <td colspan="7" class="text-center text-danger">
                    <i class="bi bi-exclamation-triangle"></i> ${escapeHtml(message)}
                </td>
            </tr>
        `;
    }
}

// 计算时间差
function getTimeAgo(timestamp) {
    const now = new Date();
    const time = parseApiDate(timestamp);
    if (!time) {
        return '-';
    }

    // 计算时间差（毫秒）
    const diffInMs = now - time;
    const diffInSeconds = Math.floor(diffInMs / 1000);

    // 如果时间差为负数，说明时间在未来，显示为"刚刚"
    if (diffInSeconds < 0) {
        return '刚刚';
    }

    if (diffInSeconds < 60) {
        return '刚刚';
    } else if (diffInSeconds < 3600) {
        const minutes = Math.floor(diffInSeconds / 60);
        return `${minutes}分钟前`;
    } else if (diffInSeconds < 86400) {
        const hours = Math.floor(diffInSeconds / 3600);
        return `${hours}小时前`;
    } else if (diffInSeconds < 2592000) {
        const days = Math.floor(diffInSeconds / 86400);
        return `${days}天前`;
    } else {
        return formatDateTime(timestamp);
    }
}

function getLicenseTypeText(keyType) {
    const typeMap = {
        'EDITOR': '编辑器',
        'EXECUTOR': '执行器'
    };
    return typeMap[keyType] || keyType;
}

function formatUptime(timestamp) {
    const numericTimestamp = Number(timestamp);
    if (Number.isFinite(numericTimestamp) && String(timestamp).trim() !== '') {
        return formatDurationFromSeconds(numericTimestamp);
    }

    const start = parseApiDate(timestamp);
    if (!start) {
        return '-';
    }

    const diffSeconds = Math.max(0, Math.floor((Date.now() - start.getTime()) / 1000));
    return formatDurationFromSeconds(diffSeconds);
}

function formatExpireDuration(expireDays) {
    if (!expireDays) return '永久';

    if (expireDays < 7) {
        return `${expireDays}天`;
    } else if (expireDays < 30) {
        const weeks = Math.floor(expireDays / 7);
        const days = expireDays % 7;
        return weeks > 0 ? (days > 0 ? `${weeks}周${days}天` : `${weeks}周`) : `${days}天`;
    } else if (expireDays < 365) {
        const months = Math.floor(expireDays / 30);
        const days = expireDays % 30;
        return months > 0 ? (days > 0 ? `${months}月${days}天` : `${months}月`) : `${days}天`;
    } else {
        const years = Math.floor(expireDays / 365);
        const days = expireDays % 365;
        return years > 0 ? (days > 0 ? `${years}年${days}天` : `${years}年`) : `${days}天`;
    }
}

function getExpireStatusBadge(expiresAt) {
    if (!expiresAt) {
        return '<span class="badge bg-success">永久</span>';
    }

    const now = new Date();
    const expireDate = new Date(expiresAt);
    const diffMs = expireDate - now;
    const diffDays = Math.ceil(diffMs / (1000 * 60 * 60 * 24));

    if (diffDays < 0) {
        return '<span class="badge bg-danger">已过期</span>';
    } else if (diffDays <= 7) {
        return `<span class="badge bg-warning">还有${diffDays}天</span>`;
    } else if (diffDays <= 30) {
        return `<span class="badge bg-info">还有${diffDays}天</span>`;
    } else {
        return `<span class="badge bg-secondary">${formatDateTime(expiresAt)}</span>`;
    }
}

function showAlert(message, type = 'info') {
    const alertHtml = `
        <div class="alert alert-${type} alert-dismissible fade show" role="alert">
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
    `;
    
    // 在主内容区域顶部显示警告
    const mainContent = document.querySelector('.main-content');
    const existingAlert = mainContent.querySelector('.alert');
    if (existingAlert) {
        existingAlert.remove();
    }
    
    mainContent.insertAdjacentHTML('afterbegin', alertHtml);
    
    // 3秒后自动消失
    setTimeout(() => {
        const alert = mainContent.querySelector('.alert');
        if (alert) {
            alert.remove();
        }
    }, 3000);
}

// 加载客户端列表
async function loadClients() {
    try {
        // 同时加载客户端和封禁列表
        const [clientsResponse, bannedResponse] = await Promise.all([
            fetch('/api/admin/clients', { credentials: 'include', cache: 'no-cache' }),
            fetch('/api/admin/banned_hardware_ids', { credentials: 'include', cache: 'no-cache' })
        ]);

        const clientsData = await clientsResponse.json();
        const bannedData = await bannedResponse.json();

        if (clientsData.success) {
            const tableBody = document.getElementById('clients-table');
            if (clientsData.clients.length === 0) {
                tableBody.innerHTML = '<tr><td colspan="7" class="text-center text-muted">暂无客户端数据</td></tr>';
                return;
            }

            // 创建封禁状态映射
            const bannedMap = new Map();
            if (bannedData.success) {
                bannedData.banned_hardware_ids.forEach(ban => {
                    if (ban.is_active) {
                        bannedMap.set(ban.hardware_id, ban);
                    }
                });
            }

            const rows = clientsData.clients.map(client => {
                const now = new Date();
                const lastSeen = client.last_seen ? new Date(client.last_seen) : null;
                const isOnline = lastSeen && (now - lastSeen) / (1000 * 60 * 60) <= 24; // 24小时内为在线

                // 检查是否被封禁
                const banInfo = bannedMap.get(client.hardware_id);
                const isBanned = !!banInfo;

                return `
                    <tr class="${isBanned ? 'table-danger' : ''}">
                        <td>
                            <div class="hardware-id-display" title="点击查看完整硬件ID" data-hardware-id="${client.hardware_id}" onclick="showFullHardwareId(this.dataset.hardwareId)">
                                ${client.hardware_id}
                            </div>
                        </td>
                        <td>${formatDateTime(client.registration_date)}</td>
                        <td>
                            ${client.last_seen ? formatDateTime(client.last_seen) : '<span class="text-muted">从未</span>'}
                        </td>
                        <td>
                            <span class="badge bg-info">${client.license_count}</span>
                        </td>
                        <td>
                            <span class="badge ${isOnline ? 'bg-success' : 'bg-secondary'}">
                                ${isOnline ? '在线' : '离线'}
                            </span>
                        </td>
                        <td>
                            ${isBanned ?
                                `<div class="d-flex align-items-center">
                                    <span class="badge bg-danger me-2" title="封禁原因: ${banInfo.reason || '未知原因'}">
                                        <i class="bi bi-shield-x"></i> 已封禁
                                    </span>
                                    <small class="text-muted" title="封禁原因: ${banInfo.reason || '未知原因'}" style="cursor: help;">
                                        ${(banInfo.reason || '未知原因').length > 15 ?
                                            (banInfo.reason || '未知原因').substring(0, 15) + '...' :
                                            (banInfo.reason || '未知原因')
                                        }
                                    </small>
                                </div>` :
                                '<span class="badge bg-success"><i class="bi bi-check-circle"></i> 正常</span>'
                            }
                        </td>
                        <td>
                            <div class="btn-group btn-group-sm">
                                <button class="btn btn-outline-info" data-hardware-id="${client.hardware_id}" onclick="viewClientDetails(this.dataset.hardwareId)" title="详情">
                                    <i class="bi bi-eye"></i>
                                </button>
                                ${isBanned ?
                                    `<button class="btn btn-outline-success" data-hardware-id="${client.hardware_id}" onclick="quickUnbanClient(this.dataset.hardwareId)" title="解除封禁">
                                        <i class="bi bi-shield-check"></i>
                                    </button>` :
                                    `<button class="btn btn-outline-warning" data-hardware-id="${client.hardware_id}" onclick="quickBanClient(this.dataset.hardwareId)" title="封禁">
                                        <i class="bi bi-shield-x"></i>
                                    </button>`
                                }
                                <button class="btn btn-outline-danger" data-hardware-id="${client.hardware_id}" onclick="removeClient(this.dataset.hardwareId)" title="移除">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </div>
                        </td>
                    </tr>
                `;
            }).join('');

            tableBody.innerHTML = rows;

            // 自动显示统计信息
            filterClientsByStatus('all');
        } else {
            showAlert('加载客户端列表失败', 'danger');
        }
    } catch (error) {
        console.error('加载客户端列表失败:', error);
        showAlert('加载客户端列表失败', 'danger');
    }
}

// 加载用户列表
async function loadUsers() {
    try {
        // 模拟用户数据（实际应该从API获取）
        const users = [
            {
                id: 1,
                username: 'admin',
                is_admin: true,
                hardware_id: null,
                created_at: '2025-07-25T15:00:00',
                last_login: '2025-07-25T23:28:00'
            }
        ];

        const tableBody = document.getElementById('users-table');
        if (users.length === 0) {
            tableBody.innerHTML = '<tr><td colspan="6" class="text-center text-muted">暂无用户数据</td></tr>';
            return;
        }

        const rows = users.map(user => `
            <tr>
                <td>
                    <strong>${user.username}</strong>
                </td>
                <td>
                    <span class="badge ${user.is_admin ? 'bg-danger' : 'bg-secondary'}">
                        ${user.is_admin ? '管理员' : '普通用户'}
                    </span>
                </td>
                <td>
                    ${user.hardware_id ?
                        `<code class="text-truncate-custom" title="${user.hardware_id}">${user.hardware_id}</code>` :
                        '<span class="text-muted">未绑定</span>'
                    }
                </td>
                <td>${formatDateTime(user.created_at)}</td>
                <td>${user.last_login ? formatDateTime(user.last_login) : '<span class="text-muted">从未</span>'}</td>
                <td>
                    <button class="btn btn-sm btn-outline-primary me-1" onclick="editUser('${user.id}')" title="编辑">
                        <i class="bi bi-pencil"></i>
                    </button>
                    ${user.username !== 'admin' ? `
                        <button class="btn btn-sm btn-outline-danger" onclick="deleteUser('${user.id}')" title="删除">
                            <i class="bi bi-trash"></i>
                        </button>
                    ` : ''}
                </td>
            </tr>
        `).join('');

        tableBody.innerHTML = rows;
    } catch (error) {
        console.error('加载用户列表失败:', error);
        showAlert('加载用户列表失败', 'danger');
    }
}

// 加载系统日志
async function loadLogs() {
    try {
        const container = document.getElementById('logs-container');

        // 显示加载状态
        container.innerHTML = `
            <div class="loading text-center">
                <div class="spinner-border text-light" role="status">
                    <span class="visually-hidden">加载中...</span>
                </div>
                <div class="mt-2 text-light">正在加载系统日志...</div>
            </div>
        `;

        // 获取日志级别过滤器
        const levelFilter = document.getElementById('logLevel')?.value || '';

        // 构建API URL
        let apiUrl = '/api/admin/logs?limit=200';
        if (levelFilter && levelFilter !== 'ALL') {
            apiUrl += `&level=${levelFilter}`;
        }

        console.log('正在请求日志API:', apiUrl);

        const response = await fetch(apiUrl, {
            credentials: 'include'
        });

        console.log('日志API响应状态:', response.status, response.statusText);

        if (!response.ok) {
            const errorText = await response.text();
            console.error('日志API错误响应:', errorText);
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }

        const data = await response.json();
        console.log('日志API响应数据:', data);

        if (!data.success) {
            throw new Error(data.message || '获取日志失败');
        }

        const logs = data.logs || [];

        if (logs.length === 0) {
            container.innerHTML = '<div class="text-center text-muted">暂无日志记录</div>';
            return;
        }

        const logHtml = logs.map(log => {
            const levelColor = {
                'INFO': '#4CAF50',
                'WARNING': '#FF9800',
                'ERROR': '#F44336',
                'DEBUG': '#2196F3'
            }[log.level] || '#888';

            const levelIcon = {
                'INFO': 'bi-info-circle',
                'WARNING': 'bi-exclamation-triangle',
                'ERROR': 'bi-x-circle',
                'DEBUG': 'bi-bug'
            }[log.level] || 'bi-circle';

            return `
                <div style="margin-bottom: 10px; font-size: 13px; line-height: 1.4; border-left: 3px solid ${levelColor}; padding-left: 10px;">
                    <div style="margin-bottom: 2px;">
                        <span style="color: #888; font-family: monospace;">${formatDateTime(log.timestamp)}</span>
                        <span style="color: ${levelColor}; font-weight: bold; margin-left: 10px;">
                            <i class="bi ${levelIcon}"></i> [${log.level}]
                        </span>
                        ${log.location ? `<span style="color: #666; margin-left: 10px; font-size: 11px;">[${log.location}]</span>` : ''}
                    </div>
                    <div style="color: #ddd; margin-left: 20px;">${escapeHtml(log.message)}</div>
                    ${log.file ? `<div style="color: #555; font-size: 11px; margin-left: 20px; margin-top: 2px;">📁 ${log.file}</div>` : ''}
                </div>
            `;
        }).join('');

        container.innerHTML = logHtml;

        // 自动滚动到顶部（显示最新日志）
        container.scrollTop = 0;

        console.log(`已加载 ${logs.length} 条日志记录`);

    } catch (error) {
        console.error('加载日志失败:', error);
        document.getElementById('logs-container').innerHTML =
            `<div class="text-center text-danger">
                <i class="bi bi-exclamation-triangle"></i>
                加载日志失败: ${error.message}
            </div>`;
    }
}

// 加载系统设置
async function loadSettings() {
    try {
        const [healthResponse, settingsResponse] = await Promise.all([
            fetch('/health', { credentials: 'include' }),
            fetch('/api/admin/settings', { credentials: 'include' })
        ]);

        if (healthResponse.ok) {
            const healthData = await healthResponse.json();
            const startupSource = healthData.startup_time || healthData.timestamp;
            if (startupSource) {
                document.getElementById('startupTime').textContent = formatDateTime(startupSource);
            }
            const uptimeSource = (healthData.uptime_seconds ?? startupSource);
            if (uptimeSource !== undefined && uptimeSource !== null) {
                document.getElementById('uptime').textContent = formatUptime(uptimeSource);
            }
            if (healthData.server_name) {
                const serverNameInput = document.getElementById('serverName');
                if (serverNameInput && !serverNameInput.value) {
                    serverNameInput.value = healthData.server_name;
                }
            }
            const serverVersionElement = document.getElementById('serverVersion');
            if (serverVersionElement && healthData.version) {
                serverVersionElement.textContent = healthData.version;
            }
            const databaseTypeElement = document.getElementById('databaseType');
            if (databaseTypeElement && healthData.database_type) {
                databaseTypeElement.textContent = healthData.database_type;
            }
            const pythonVersionElement = document.getElementById('pythonVersion');
            if (pythonVersionElement && healthData.python_version) {
                pythonVersionElement.textContent = healthData.python_version;
            }
            const fastapiVersionElement = document.getElementById('fastapiVersion');
            if (fastapiVersionElement && healthData.fastapi_version) {
                fastapiVersionElement.textContent = healthData.fastapi_version;
            }
        }

        const settingsData = await settingsResponse.json();
        if (!settingsResponse.ok || !settingsData.success || !settingsData.settings) {
            throw new Error(settingsData.detail || settingsData.message || '加载系统设置失败');
        }

        const settings = settingsData.settings;
        document.getElementById('serverName').value = settings.serverName ?? '';
        document.getElementById('maxClients').value = settings.maxClients ?? 1000;
        document.getElementById('sessionTimeout').value = settings.sessionTimeout ?? 60;
        document.getElementById('marketUpdateServerBase').value = settings.marketUpdateServerBase ?? '';
        document.getElementById('enableLogging').checked = Boolean(settings.enableLogging);
        document.getElementById('maxLoginAttempts').value = settings.maxLoginAttempts ?? 5;
        document.getElementById('lockoutDuration').value = settings.lockoutDuration ?? 30;
        document.getElementById('enableCSRF').checked = Boolean(settings.enableCSRF);
        document.getElementById('enableRateLimit').checked = Boolean(settings.enableRateLimit);

        // 检查二级密码状态
        await checkSecondaryPasswordStatus();
        await loadLicenseValidationStatus();

    } catch (error) {
        console.error('加载系统设置失败:', error);
        showAlert(error.message || '加载系统设置失败', 'danger');
    }
}

// 查看许可证详情
async function viewLicenseDetails(licenseId) {
    try {
        const response = await fetch(`/api/admin/license/${licenseId}`);
        const data = await response.json();

        if (data.success) {
            const license = data.license;
            const isEditor = String(license.key_type || '').toUpperCase() === 'EDITOR';
            const safeMainKey = escapeHtml(String(license.key_string || ''));
            const safeMainHardwareId = license.client_hardware_id ? escapeHtml(String(license.client_hardware_id)) : '';
            const activeExecutorCount = Number.isFinite(Number(license.active_executor_count)) ? Number(license.active_executor_count) : 0;
            const managedExecutorLimit = Number.isFinite(Number(license.managed_executor_limit)) ? Number(license.managed_executor_limit) : null;

            const childLicenses = Array.isArray(license.child_licenses) ? license.child_licenses : [];
            const childRowsHtml = childLicenses.length > 0 ? childLicenses.map(child => `
                <tr>
                    <td>${child.id}</td>
                    <td>
                        <div class="license-detail-key-wrap">
                            <code class="license-detail-key-code">${escapeHtml(String(child.key_string || ''))}</code>
                            <button class="btn btn-sm btn-outline-secondary" data-license-key="${escapeHtml(String(child.key_string || ''))}" onclick="copyToClipboard(this.dataset.licenseKey)">
                                <i class="bi bi-clipboard"></i>
                            </button>
                        </div>
                    </td>
                    <td>${child.client_hardware_id ? `<code class="license-detail-key-code">${escapeHtml(String(child.client_hardware_id))}</code>` : '<span class="text-muted">未绑定</span>'}</td>
                    <td>${child.created_at ? formatDateTime(child.created_at) : '-'}</td>
                    <td>${child.expires_at ? formatDateTime(child.expires_at) : '<span class="badge bg-success">永久</span>'}</td>
                    <td><span class="badge ${child.is_active ? 'bg-success' : 'bg-danger'}">${child.is_active ? '活跃' : '禁用'}</span></td>
                </tr>
            `).join('') : `
                <tr>
                    <td colspan="6" class="text-center text-muted">暂无子授权码</td>
                </tr>
            `;
            const detailsHtml = `
                <div class="row">
                    <div class="col-md-6">
                        <table class="table table-borderless license-detail-table">
                            <tr>
                                <th>许可证ID</th>
                                <td>${license.id}</td>
                            </tr>
                            <tr>
                                <th>许可证密钥</th>
                                <td>
                                    <div class="license-detail-key-wrap">
                                        <code class="license-detail-key-code">${safeMainKey}</code>
                                        <button class="btn btn-sm btn-outline-secondary" data-license-key="${safeMainKey}" onclick="copyToClipboard(this.dataset.licenseKey)">
                                            <i class="bi bi-clipboard"></i>
                                        </button>
                                    </div>
                                </td>
                            </tr>
                            <tr>
                                <th>类型</th>
                                <td><span class="badge bg-primary">${getLicenseTypeText(license.key_type)}</span></td>
                            </tr>
                            <tr>
                                <th>状态</th>
                                <td><span class="badge ${license.is_active ? 'bg-success' : 'bg-danger'}">${license.is_active ? '活跃' : '禁用'}</span></td>
                            </tr>
                            <tr>
                                <th>创建时间</th>
                                <td>${formatDateTime(license.created_at)}</td>
                            </tr>
                            <tr>
                                <th>过期时间</th>
                                <td>${license.expires_at ? formatDateTime(license.expires_at) : '<span class="badge bg-success">永久</span>'}</td>
                            </tr>
                        </table>
                    </div>
                    <div class="col-md-6">
                        <table class="table table-borderless license-detail-table">
                            <tr>
                                <th>绑定客户端</th>
                                <td>${safeMainHardwareId ? `<code class="license-detail-key-code">${safeMainHardwareId}</code>` : '<span class="text-muted">未绑定</span>'}</td>
                            </tr>
                            <tr>
                                <th>当前激活</th>
                                <td>${license.current_activations}</td>
                            </tr>
                            <tr>
                                <th>最大激活</th>
                                <td>${license.max_activations}</td>
                            </tr>
                            ${isEditor ? `
                                <tr>
                                    <th>子码上限</th>
                                    <td>${managedExecutorLimit === null ? '-' : (managedExecutorLimit === 0 ? '不限制' : managedExecutorLimit)}</td>
                                </tr>
                                <tr>
                                    <th>子码数量</th>
                                    <td>${activeExecutorCount}</td>
                                </tr>
                            ` : ''}
                            ${license.client_info ? `
                                <tr>
                                    <th>客户端注册</th>
                                    <td>${formatDateTime(license.client_info.registration_date)}</td>
                                </tr>
                                <tr>
                                    <th>最后活动</th>
                                    <td>${license.client_info.last_seen ? formatDateTime(license.client_info.last_seen) : '<span class="text-muted">从未</span>'}</td>
                                </tr>
                            ` : ''}
                        </table>
                    </div>
                </div>
                ${isEditor ? `
                    <div class="row mt-3">
                        <div class="col-12">
                            <h6 class="mb-2">子授权码（执行器）</h6>
                            <div class="table-responsive">
                                <table class="table table-sm table-bordered align-middle">
                                    <thead>
                                        <tr>
                                            <th>ID</th>
                                            <th>授权码</th>
                                            <th>绑定客户端</th>
                                            <th>创建时间</th>
                                            <th>过期时间</th>
                                            <th>状态</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        ${childRowsHtml}
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                ` : ''}
            `;

            document.getElementById('licenseDetailsContent').innerHTML = detailsHtml;
            new bootstrap.Modal(document.getElementById('licenseDetailsModal')).show();
        } else {
            showAlert('获取许可证详情失败', 'danger');
        }
    } catch (error) {
        console.error('获取许可证详情失败:', error);
        showAlert('获取许可证详情失败', 'danger');
    }
}

// 编辑许可证
async function editLicense(licenseId) {
    try {
        const response = await fetch(`/api/admin/license/${licenseId}`);
        const data = await response.json();

        if (data.success) {
            const license = data.license;

            // 填充编辑表单
            document.getElementById('editLicenseId').value = license.id;
            document.getElementById('editLicenseKey').value = license.key_string;
            document.getElementById('editLicenseType').value = license.key_type;
            document.getElementById('editClientHardwareId').value = license.client_hardware_id || '';
            document.getElementById('editMaxActivations').value = license.max_activations;
            document.getElementById('editIsActive').checked = license.is_active;
            document.getElementById('editExecutorParentLicenseKey').value = license.parent_license_key || '';

            // 处理过期时间设置
            if (license.expires_at) {
                document.getElementById('editExpireType').value = 'custom_date';
                const expireDate = new Date(license.expires_at);
                // 转换为本地时间格式
                const localDateTime = new Date(expireDate.getTime() - expireDate.getTimezoneOffset() * 60000)
                    .toISOString().slice(0, 16);
                document.getElementById('editExpireDate').value = localDateTime;
            } else {
                document.getElementById('editExpireType').value = 'permanent';
                document.getElementById('editExpireDate').value = '';
            }

            // 触发显示/隐藏相关控件
            toggleEditExpireSettings();
            toggleEditLicenseTypeFields(license.key_type);

            // 显示编辑模态框
            new bootstrap.Modal(document.getElementById('editLicenseModal')).show();
        } else {
            showAlert('获取许可证信息失败', 'danger');
        }
    } catch (error) {
        console.error('获取许可证信息失败:', error);
        showAlert('获取许可证信息失败', 'danger');
    }
}

// 计算新的过期时间
function calculateNewExpireTime(currentExpireTime) {
    const expireType = document.getElementById('editExpireType').value;

    if (expireType === 'permanent') {
        return null; // 永久有效
    } else if (expireType === 'custom_date') {
        const expireDate = document.getElementById('editExpireDate').value;
        return expireDate || null;
    } else if (expireType === 'extend') {
        const value = parseInt(document.getElementById('editExtendValue').value);
        const unit = document.getElementById('editExtendUnit').value;

        if (!value || value <= 0) {
            showAlert('请输入有效的延长期限', 'warning');
            return undefined; // 表示输入无效
        }

        // 计算延长的毫秒数
        let extendMs = 0;
        switch (unit) {
            case 'days':
                extendMs = value * 24 * 60 * 60 * 1000;
                break;
            case 'weeks':
                extendMs = value * 7 * 24 * 60 * 60 * 1000;
                break;
            case 'months':
                extendMs = value * 30 * 24 * 60 * 60 * 1000; // 近似值
                break;
            case 'years':
                extendMs = value * 365 * 24 * 60 * 60 * 1000; // 近似值
                break;
            default:
                extendMs = value * 24 * 60 * 60 * 1000; // 默认按天计算
        }

        // 基于当前过期时间或当前时间延长
        const baseTime = currentExpireTime ? new Date(currentExpireTime) : new Date();
        const newExpireTime = new Date(baseTime.getTime() + extendMs);

        return newExpireTime.toISOString();
    }

    return null;
}

// 更新许可证
async function updateLicense() {
    const licenseId = document.getElementById('editLicenseId').value;
    const licenseType = String(document.getElementById('editLicenseType').value || '').toUpperCase();
    const clientHardwareId = document.getElementById('editClientHardwareId').value.trim();
    const maxActivationsRaw = document.getElementById('editMaxActivations').value;
    const maxActivations = parseInt(maxActivationsRaw, 10);
    const isActive = document.getElementById('editIsActive').checked;
    const parentLicenseKey = document.getElementById('editExecutorParentLicenseKey').value.trim();

    if (Number.isNaN(maxActivations)) {
        showAlert('最大激活数量必须为整数', 'warning');
        return;
    }

    if (licenseType === 'EDITOR' && maxActivations < 0) {
        showAlert('编辑器可管理执行器数量不能为负数', 'warning');
        return;
    }

    if (licenseType !== 'EDITOR' && maxActivations < 1) {
        showAlert('最大激活数量必须大于等于1', 'warning');
        return;
    }

    // 验证硬件ID格式
    if (clientHardwareId && clientHardwareId.length !== 64) {
        showAlert('硬件ID必须是64字符的SHA256值', 'warning');
        return;
    }

    // 获取当前许可证信息以计算新的过期时间
    let currentExpireTime = null;
    try {
        const currentResponse = await fetch(`/api/admin/license/${licenseId}`);
        const currentData = await currentResponse.json();
        if (currentData.success) {
            currentExpireTime = currentData.license.expires_at;
        }
    } catch (error) {
        console.error('获取当前许可证信息失败:', error);
    }

    const newExpireTime = calculateNewExpireTime(currentExpireTime);
    if (newExpireTime === undefined) {
        return; // 输入验证失败
    }

    const updateData = {
        expires_at: newExpireTime,
        client_hardware_id: clientHardwareId || null,
        is_active: isActive
    };

    if (licenseType === 'EDITOR') {
        updateData.managed_executor_limit = maxActivations;
    } else {
        updateData.max_activations = maxActivations;
        if (licenseType === 'EXECUTOR' && parentLicenseKey) {
            updateData.parent_license_key = parentLicenseKey;
        }
    }

    try {
        const response = await fetch(`/api/admin/license/${licenseId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(updateData)
        });

        const data = await response.json();

        if (response.ok && data.success) {
            showAlert('许可证更新成功', 'success');
            bootstrap.Modal.getInstance(document.getElementById('editLicenseModal')).hide();
            loadLicenses(); // 刷新列表
        } else {
            showAlert(data.detail || data.message || '许可证更新失败', 'danger');
        }
    } catch (error) {
        console.error('许可证更新失败:', error);
        showAlert('许可证更新失败: ' + (error.message || '未知错误'), 'danger');
    }
}

// 删除许可证
async function deleteLicense(licenseId, licenseKey) {
    const maskedKey = licenseKey.substring(0, 8) + '***';
    if (confirm(`确定要删除许可证 ${maskedKey} 吗？\n\n此操作不可撤销，将会：\n• 删除许可证记录\n• 解除客户端绑定\n• 使该许可证立即失效`)) {
        try {
            const result = await sendDeleteRequestWithSecondaryVerification(`/api/admin/license/${licenseId}`, '删除许可证');
            if (result.cancelled) {
                return;
            }
            const { response, data } = result;

            if (response.ok && data.success) {
                showAlert('许可证删除成功', 'success');
                loadLicenses(); // 刷新列表
            } else {
                throw new Error(data.detail || data.message || '删除失败');
            }
        } catch (error) {
            console.error('许可证删除失败:', error);
            showAlert('许可证删除失败: ' + error.message, 'danger');
        }
    }
}

function copyLicenseKey(licenseKey) {
    copyToClipboard(licenseKey, '\u8bb8\u53ef\u8bc1\u5bc6\u94a5\u5df2\u590d\u5236\u5230\u526a\u8d34\u677f');
}


// ==================== 封禁管理功能 ====================

// 加载封禁列表
async function loadBannedList() {
    try {
        showLoading('banned-table');

        const response = await fetch('/api/admin/banned_hardware_ids', {
            method: 'GET',
            credentials: 'include',
            cache: 'no-cache'
        });

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        const data = await response.json();

        if (data.success) {
            displayBannedList(data.banned_hardware_ids);
        } else {
            throw new Error(data.message || '获取封禁列表失败');
        }
    } catch (error) {
        console.error('加载封禁列表失败:', error);
        showError('banned-table', '加载封禁列表失败: ' + error.message);
    }
}

// 显示封禁列表
function displayBannedList(bannedList) {
    const tbody = document.getElementById('banned-table');

    if (!bannedList || bannedList.length === 0) {
        tbody.innerHTML = `
            <tr>
                <td colspan="7" class="text-center text-muted">
                    <i class="bi bi-inbox"></i> 暂无封禁记录
                </td>
            </tr>
        `;
        return;
    }

    tbody.innerHTML = bannedList.map(ban => `
        <tr>
            <td>
                <div class="hardware-id-display" title="点击查看完整硬件ID" data-hardware-id="${ban.hardware_id}" onclick="showFullHardwareId(this.dataset.hardwareId)">
                    ${ban.hardware_id}
                </div>
            </td>
            <td>${ban.reason || '-'}</td>
            <td>${formatDateTime(ban.banned_at)}</td>
            <td>${ban.banned_by || '-'}</td>
            <td>${ban.expires_at ? formatDateTime(ban.expires_at) : '永久'}</td>
            <td>
                <span class="badge ${ban.is_active ? 'bg-danger' : 'bg-secondary'}">
                    ${ban.is_active ? '生效中' : '已禁用'}
                </span>
            </td>
            <td>
                <div class="btn-group btn-group-sm">
                    <button class="btn btn-outline-warning" onclick="toggleBanStatus(${ban.id})"
                            title="${ban.is_active ? '禁用封禁' : '启用封禁'}">
                        <i class="bi bi-${ban.is_active ? 'pause' : 'play'}"></i>
                    </button>
                    <button class="btn btn-outline-danger" onclick="deleteBanRecord(${ban.id})"
                            title="删除记录">
                        <i class="bi bi-trash"></i>
                    </button>
                </div>
            </td>
        </tr>
    `).join('');
}

// 封禁硬件ID
async function banHardwareId() {
    const hardwareId = document.getElementById('banHardwareId').value.trim();
    const reason = document.getElementById('banReason').value.trim();
    const duration = document.getElementById('banDuration').value;
    const notes = document.getElementById('banNotes').value.trim();

    console.log('封禁硬件ID函数调用');
    console.log('原始硬件ID:', document.getElementById('banHardwareId').value);
    console.log('处理后硬件ID:', hardwareId, '长度:', hardwareId.length);

    // 验证输入
    if (!hardwareId) {
        showAlert('请输入硬件ID', 'warning');
        return;
    }

    if (!/^[a-fA-F0-9]{64}$/.test(hardwareId)) {
        console.log('硬件ID格式验证失败:', hardwareId);
        showAlert(`硬件ID格式无效，必须是64字符的十六进制字符串\n当前输入: ${hardwareId}\n长度: ${hardwareId.length}`, 'warning');
        return;
    }

    if (!reason) {
        showAlert('请输入封禁原因', 'warning');
        return;
    }

    try {
        const requestData = {
            hardware_id: hardwareId,
            reason: reason,
            notes: notes
        };

        if (duration) {
            requestData.expires_days = parseInt(duration);
        }

        const response = await fetch('/api/admin/ban_hardware_id', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            credentials: 'include',
            body: JSON.stringify(requestData)
        });

        const data = await response.json();

        if (response.ok && data.success) {
            showAlert(data.message || '硬件ID封禁成功', 'success');

            // 关闭模态框
            const modal = bootstrap.Modal.getInstance(document.getElementById('banHardwareModal'));
            modal.hide();

            // 清空表单
            document.getElementById('banHardwareForm').reset();

            // 刷新列表
            loadBannedList();
            loadClients(); // 同时刷新客户端列表
        } else {
            // 处理特定的错误情况
            if (response.status === 409) {
                showAlert(`该硬件ID已被封禁\n硬件ID: ${hardwareId}\n请先解除现有封禁再重新封禁`, 'warning');
            } else {
                throw new Error(data.detail || data.message || '封禁失败');
            }
        }
    } catch (error) {
        console.error('封禁硬件ID失败:', error);
        showAlert('封禁失败: ' + error.message, 'danger');
    }
}

// 切换封禁状态
async function toggleBanStatus(banId) {
    if (!confirm('确定要切换此封禁记录的状态吗？')) {
        return;
    }

    try {
        const response = await fetch(`/api/admin/toggle_ban/${banId}`, {
            method: 'POST',
            credentials: 'include'
        });

        const data = await response.json();

        if (response.ok && data.success) {
            showAlert(data.message, 'success');
            loadBannedList();
        } else {
            throw new Error(data.detail || data.message || '操作失败');
        }
    } catch (error) {
        console.error('切换封禁状态失败:', error);
        showAlert('操作失败: ' + error.message, 'danger');
    }
}

// 删除封禁记录
async function deleteBanRecord(banId) {
    if (!confirm('确定要删除此封禁记录吗？删除后将无法恢复。')) {
        return;
    }

    try {
        const result = await sendDeleteRequestWithSecondaryVerification(`/api/admin/ban/${banId}`, '删除封禁记录');
        if (result.cancelled) {
            return;
        }
        const { response, data } = result;

        if (response.ok && data.success) {
            showAlert('封禁记录删除成功', 'success');
            loadBannedList();
        } else {
            throw new Error(data.detail || data.message || '删除失败');
        }
    } catch (error) {
        console.error('删除封禁记录失败:', error);
        showAlert('删除失败: ' + error.message, 'danger');
    }
}

// 快速封禁客户端
async function quickBanClient(hardwareId) {
    const reason = prompt('请输入封禁原因:', '违规使用');
    if (!reason || reason.trim() === '') {
        showAlert('封禁原因不能为空', 'warning');
        return;
    }

    if (!confirm(`确定要封禁硬件ID: ${hardwareId}\n封禁原因: ${reason}\n\n封禁后该硬件ID将无法使用任何授权功能。`)) {
        return;
    }

    try {
        const response = await fetch('/api/admin/ban_hardware_id', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            credentials: 'include',
            body: JSON.stringify({
                hardware_id: hardwareId,
                reason: reason,
                notes: '从客户端管理快速封禁'
            })
        });

        const data = await response.json();

        if (response.ok && data.success) {
            showAlert(`硬件ID封禁成功！\n硬件ID: ${hardwareId}\n封禁原因: ${reason}`, 'success');
            loadClients(); // 刷新客户端列表
        } else {
            // 处理特定的错误情况
            if (response.status === 409) {
                showAlert(`该硬件ID已被封禁\n硬件ID: ${hardwareId}\n请先解除现有封禁再重新封禁`, 'warning');
            } else {
                throw new Error(data.detail || data.message || '封禁失败');
            }
        }
    } catch (error) {
        console.error('快速封禁失败:', error);
        showAlert('封禁失败: ' + error.message, 'danger');
    }
}

// 快速解封客户端
async function quickUnbanClient(hardwareId) {
    if (!confirm(`确定要解除硬件ID: ${hardwareId} 的封禁吗？\n\n解封后该硬件ID将恢复正常使用权限。`)) {
        return;
    }

    try {
        // 首先获取封禁记录ID
        const bannedResponse = await fetch('/api/admin/banned_hardware_ids', {
            credentials: 'include'
        });
        const bannedData = await bannedResponse.json();

        if (!bannedData.success) {
            throw new Error('获取封禁列表失败');
        }

        const banRecord = bannedData.banned_hardware_ids.find(ban =>
            ban.hardware_id === hardwareId && ban.is_active
        );

        if (!banRecord) {
            throw new Error('找不到对应的封禁记录');
        }

        const response = await fetch(`/api/admin/unban_hardware_id/${banRecord.id}`, {
            method: 'POST',
            credentials: 'include'
        });

        const data = await response.json();

        if (response.ok && data.success) {
            showAlert(`硬件ID解封成功！\n硬件ID: ${hardwareId}\n该硬件ID已恢复正常使用权限`, 'success');
            loadClients(); // 刷新客户端列表
        } else {
            throw new Error(data.detail || data.message || '解封失败');
        }
    } catch (error) {
        console.error('快速解封失败:', error);
        showAlert('解封失败: ' + error.message, 'danger');
    }
}

// 预填充封禁模态框
function prefillBanModal(hardwareId = '') {
    console.log('预填充封禁模态框，硬件ID:', hardwareId, '长度:', hardwareId.length);

    const hardwareIdInput = document.getElementById('banHardwareId');
    if (hardwareIdInput) {
        hardwareIdInput.value = hardwareId;
        console.log('设置后的输入框值:', hardwareIdInput.value, '长度:', hardwareIdInput.value.length);
    } else {
        console.error('找不到硬件ID输入框');
    }

    document.getElementById('banReason').value = '';
    document.getElementById('banDuration').value = '';
    document.getElementById('banNotes').value = '';

    // 显示模态框
    const modal = new bootstrap.Modal(document.getElementById('banHardwareModal'));
    modal.show();
}

// 显示完整硬件ID
function showFullHardwareId(hardwareId) {
    console.log('显示完整硬件ID:', hardwareId, '长度:', hardwareId.length);

    const modalHtml = `
        <div class="modal fade" id="hardwareIdModal" tabindex="-1">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title">
                            <i class="bi bi-cpu"></i> 完整硬件ID
                        </h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                    </div>
                    <div class="modal-body">
                        <div class="mb-3">
                            <label class="form-label">硬件ID:</label>
                            <div class="hardware-id-full" id="fullHardwareId">${hardwareId}</div>
                        </div>
                        <div class="d-grid gap-2">
                            <button class="btn btn-outline-primary" data-hardware-id="${hardwareId}" onclick="copyToClipboard(this.dataset.hardwareId)">
                                <i class="bi bi-clipboard"></i> 复制到剪贴板
                            </button>
                            <button class="btn btn-outline-warning" data-hardware-id="${hardwareId}" onclick="prefillBanModal(this.dataset.hardwareId); bootstrap.Modal.getInstance(document.getElementById('hardwareIdModal')).hide();">
                                <i class="bi bi-shield-x"></i> 封禁此硬件ID
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `;

    // 移除已存在的模态框
    const existingModal = document.getElementById('hardwareIdModal');
    if (existingModal) {
        existingModal.remove();
    }

    // 添加新模态框
    document.body.insertAdjacentHTML('beforeend', modalHtml);

    // 显示模态框
    const modal = new bootstrap.Modal(document.getElementById('hardwareIdModal'));
    modal.show();

    // 模态框关闭后移除DOM元素
    modal._element.addEventListener('hidden.bs.modal', function () {
        this.remove();
    });
}

// 复制到剪贴板
async function copyToClipboard(text, successMessage = '\u5185\u5bb9\u5df2\u590d\u5236\u5230\u526a\u8d34\u677f') {
    const resolvedMessage = String(successMessage || '').trim() || '\u5185\u5bb9\u5df2\u590d\u5236\u5230\u526a\u8d34\u677f';
    try {
        await navigator.clipboard.writeText(text);
        showAlert(resolvedMessage, 'success');
    } catch (err) {
        const textArea = document.createElement('textarea');
        textArea.value = text;
        textArea.style.position = 'fixed';
        textArea.style.left = '-999999px';
        textArea.style.top = '-999999px';
        document.body.appendChild(textArea);
        textArea.focus();
        textArea.select();

        try {
            document.execCommand('copy');
            showAlert(resolvedMessage, 'success');
        } catch (err) {
            showAlert('\u590d\u5236\u5931\u8d25\uff0c\u8bf7\u624b\u52a8\u590d\u5236', 'warning');
        }

        textArea.remove();
    }
}

/**
 * \u4fee\u6539\u7ba1\u7406\u5458\u5bc6\u7801
 */
async function changeAdminPassword() {
    const currentPassword = document.getElementById('currentPassword').value;
    const newPassword = document.getElementById('newPassword').value;
    const confirmNewPassword = document.getElementById('confirmNewPassword').value;

    if (!currentPassword || !newPassword || !confirmNewPassword) {
        showAlert('\u8bf7\u586b\u5199\u6240\u6709\u5bc6\u7801\u5b57\u6bb5', 'warning');
        return;
    }

    if (newPassword !== confirmNewPassword) {
        showAlert('\u65b0\u5bc6\u7801\u4e0e\u786e\u8ba4\u5bc6\u7801\u4e0d\u5339\u914d', 'warning');
        return;
    }

    if (newPassword.length < 6) {
        showAlert('\u65b0\u5bc6\u7801\u957f\u5ea6\u81f3\u5c11\u4e3a6\u4e2a\u5b57\u7b26', 'warning');
        return;
    }

    if (currentPassword === newPassword) {
        showAlert('\u65b0\u5bc6\u7801\u4e0d\u80fd\u4e0e\u5f53\u524d\u5bc6\u7801\u76f8\u540c', 'warning');
        return;
    }

    try {
        const response = await fetch('/api/admin/change_password', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            credentials: 'include',
            body: JSON.stringify({
                old_password: currentPassword,
                new_password: newPassword
            })
        });

        const data = await response.json();

        if (response.ok && data.success) {
            showAlert('\u7ba1\u7406\u5458\u5bc6\u7801\u4fee\u6539\u6210\u529f\uff01\u8bf7\u4f7f\u7528\u65b0\u5bc6\u7801\u91cd\u65b0\u767b\u5f55', 'success');
            document.getElementById('changePasswordForm').reset();
            setTimeout(() => {
                window.location.href = '/login';
            }, 3000);
        } else {
            showAlert(data.detail || data.message || '\u5bc6\u7801\u4fee\u6539\u5931\u8d25', 'danger');
        }
    } catch (error) {
        console.error('\u4fee\u6539\u5bc6\u7801\u9519\u8bef:', error);
        showAlert('\u4fee\u6539\u5bc6\u7801\u65f6\u53d1\u751f\u7f51\u7edc\u9519\u8bef', 'danger');
    }
}

/**
 * 设置二级密码
 */
async function setSecondaryPassword() {
    const password = document.getElementById('secondaryPassword').value;
    const confirmPassword = document.getElementById('confirmSecondaryPassword').value;
    const oldPassword = document.getElementById('oldSecondaryPassword').value;
    const description = document.getElementById('secondaryPasswordDescription').value;

    // 验证输入
    if (!password || !confirmPassword) {
        showAlert('请填写二级密码字段', 'warning');
        return;
    }

    if (password !== confirmPassword) {
        showAlert('二级密码与确认密码不匹配', 'warning');
        return;
    }

    if (password.length < 6) {
        showAlert('二级密码长度至少为6个字符', 'warning');
        return;
    }

    // 检查是否需要旧密码
    const oldPasswordGroup = document.getElementById('oldSecondaryPasswordGroup');
    if (oldPasswordGroup.style.display !== 'none' && !oldPassword) {
        showAlert('请输入旧的二级密码', 'warning');
        return;
    }

    try {
        const requestBody = {
            password: password,
            description: description || '管理员二级密码'
        };

        // 如果有旧密码字段显示，则添加旧密码
        if (oldPasswordGroup.style.display !== 'none') {
            requestBody.old_password = oldPassword;
        }

        const response = await fetch('/api/admin/set_secondary_password', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            credentials: 'include',
            body: JSON.stringify(requestBody)
        });

        const data = await response.json();

        if (response.ok && data.success) {
            showAlert(data.message || '二级密码设置成功！', 'success');
            // 清空表单
            document.getElementById('secondaryPasswordForm').reset();
            // 重新检查二级密码状态
            await checkSecondaryPasswordStatus();
        } else {
            showAlert(data.detail || data.message || '二级密码设置失败', 'danger');
        }
    } catch (error) {
        console.error('设置二级密码错误:', error);
        showAlert('设置二级密码时发生网络错误', 'danger');
    }
}

/**
 * 检查是否已有二级密码，并更新UI
 */
async function checkSecondaryPasswordStatus() {
    try {
        const response = await fetch('/api/admin/check_secondary_password', {
            method: 'GET',
            credentials: 'include'
        });

        const data = await response.json();

        const oldPasswordGroup = document.getElementById('oldSecondaryPasswordGroup');
        const buttonText = document.getElementById('secondaryPasswordButtonText');
        const newPasswordLabel = document.querySelector('label[for="secondaryPassword"]');

        if (response.ok && data.success && data.has_secondary_password) {
            // 已有二级密码，显示旧密码输入框
            oldPasswordGroup.style.display = 'block';
            buttonText.textContent = '修改二级密码';
            if (newPasswordLabel) {
                newPasswordLabel.textContent = '新的二级密码';
            }
        } else {
            // 没有二级密码，隐藏旧密码输入框
            oldPasswordGroup.style.display = 'none';
            buttonText.textContent = '设置二级密码';
            if (newPasswordLabel) {
                newPasswordLabel.textContent = '二级密码';
            }
        }
    } catch (error) {
        console.error('检查二级密码状态失败:', error);
    }
}

/**
 * 切换许可证验证开关
 */
async function toggleLicenseValidation() {
    const switchElement = document.getElementById('licenseValidationSwitch');
    const enabled = switchElement.checked;

    // 如果是关闭操作，需要输入二级密码
    if (!enabled) {
        const secondaryPassword = prompt('关闭授权验证需要输入二级密码:');

        if (!secondaryPassword) {
            // 用户取消或未输入密码，恢复开关状态
            await loadLicenseValidationStatus();
            showAlert('已取消关闭授权验证', 'info');
            return;
        }

        try {
            const response = await fetch('/api/admin/toggle_license_validation', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                credentials: 'include',
                body: JSON.stringify({
                    enabled: enabled,
                    secondary_password: secondaryPassword
                })
            });

            const data = await response.json();

            if (response.ok && data.success) {
                await loadLicenseValidationStatus();
                showAlert(`许可证验证已关闭`, 'success');
            } else {
                await loadLicenseValidationStatus();
                showAlert(data.detail || data.message || '关闭验证状态失败', 'danger');
            }
        } catch (error) {
            console.error('切换验证状态错误:', error);
            await loadLicenseValidationStatus();
            showAlert('切换验证状态时发生网络错误', 'danger');
        }
    } else {
        // 开启操作不需要二级密码
        try {
            const response = await fetch('/api/admin/toggle_license_validation', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                credentials: 'include',
                body: JSON.stringify({
                    enabled: enabled
                })
            });

            const data = await response.json();

            if (response.ok && data.success) {
                await loadLicenseValidationStatus();
                showAlert(`许可证验证已开启`, 'success');
            } else {
                await loadLicenseValidationStatus();
                showAlert(data.detail || data.message || '开启验证状态失败', 'danger');
            }
        } catch (error) {
            console.error('切换验证状态错误:', error);
            await loadLicenseValidationStatus();
            showAlert('切换验证状态时发生网络错误', 'danger');
        }
    }
}

/**
 * 加载许可证验证状态
 */
async function loadLicenseValidationStatus() {
    try {
        // 添加时间戳参数防止浏览器缓存
        const timestamp = new Date().getTime();
        const response = await fetch(`/api/admin/get_license_validation_status?t=${timestamp}`, {
            method: 'GET',
            credentials: 'include',
            cache: 'no-cache'  // 禁用缓存
        });

        const data = await response.json();

        if (response.ok && data.success) {
            updateLicenseValidationUI(data.enabled);
        } else {
            console.error('加载验证状态失败:', data.detail || data.message);
        }
    } catch (error) {
        console.error('加载验证状态错误:', error);
    }
}

/**
 * 更新许可证验证UI显示
 */
function updateLicenseValidationUI(enabled) {
    const switchElement = document.getElementById('licenseValidationSwitch');
    const statusText = document.getElementById('licenseValidationStatusText');
    const badge = document.getElementById('licenseValidationBadge');

    if (switchElement) {
        switchElement.checked = enabled;
    }

    if (statusText) {
        if (enabled) {
            statusText.innerHTML = '<i class="bi bi-shield-check text-success"></i> <strong>密钥验证已开启</strong> - 客户端需要验证许可证密钥';
        } else {
            statusText.innerHTML = '<i class="bi bi-shield-x text-warning"></i> <strong>密钥验证已关闭</strong> - 客户端只需注册硬件ID';
        }
    }

    if (badge) {
        if (enabled) {
            badge.className = 'badge bg-success';
            badge.textContent = '验证已开启';
        } else {
            badge.className = 'badge bg-warning';
            badge.textContent = '验证已关闭';
        }
    }
}

// 在原有的 initializeApp 函数中添加验证状态加载
// 修改 switchSection 函数以在切换到设置页面时刷新验证状态
const _originalSwitchSection = window.switchSection;
if (_originalSwitchSection) {
    window.switchSection = function(section) {
        _originalSwitchSection(section);
        if (section === 'settings') {
            loadLicenseValidationStatus();
        }
    };
}
