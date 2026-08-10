// 卡密管理相关JavaScript代码
// 在admin.js中添加以下代码，或创建为单独文件引入

// ==================== 卡密管理 ====================

// 显示提示信息的辅助函数
function showAlert(message, type = 'info') {
    // 如果 admin.js 中已有 showAlert 函数，优先使用
    if (window.showAlertMessage) {
        window.showAlertMessage(message, type);
        return;
    }

    // 否则使用简单的 alert
    console.log(`[${type.toUpperCase()}] ${message}`);

    // 创建 Bootstrap 提示
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show position-fixed top-0 start-50 translate-middle-x mt-3`;
    alertDiv.style.zIndex = '9999';
    alertDiv.style.minWidth = '300px';
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;

    document.body.appendChild(alertDiv);

    // 3秒后自动消失
    setTimeout(() => {
        alertDiv.remove();
    }, 3000);
}

// 刷新卡密列表
async function refreshCards() {
    const tableBody = document.getElementById('cards-table');
    if (!tableBody) {
        console.error('找不到 cards-table 元素');
        return;
    }

    tableBody.innerHTML = '<tr><td colspan="8" class="text-center"><div class="spinner-border"></div></td></tr>';

    try {
        // 添加时间戳防止缓存
        const timestamp = new Date().getTime();
        const response = await fetch(`/api/admin/cards?limit=100&_t=${timestamp}`, {
            credentials: 'include',
            cache: 'no-cache',
            headers: {
                'Cache-Control': 'no-cache, no-store, must-revalidate',
                'Pragma': 'no-cache'
            }
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || '获取卡密列表失败');
        }

        const data = await response.json();

        // 更新统计数据
        const totalCards = document.getElementById('total-cards');
        const unusedCards = document.getElementById('unused-cards');
        const usedCards = document.getElementById('used-cards');
        const disabledCards = document.getElementById('disabled-cards');

        if (totalCards) totalCards.textContent = data.statistics.total;
        if (unusedCards) unusedCards.textContent = data.statistics.unused;
        if (usedCards) usedCards.textContent = data.statistics.used;
        if (disabledCards) disabledCards.textContent = (data.statistics.total - data.statistics.unused - data.statistics.used);

        // 清空表格
        tableBody.innerHTML = '';

        // 更新表格
        if (data.cards.length === 0) {
            tableBody.innerHTML = '<tr><td colspan="8" class="text-center text-muted">暂无卡密记录</td></tr>';
            return;
        }

        data.cards.forEach(card => {
            const row = document.createElement('tr');
            row.setAttribute('data-card-id', card.id); // 添加标识符便于删除

            // 状态徽章
            let statusBadge = '';
            switch (card.status) {
                case 'unused':
                    statusBadge = '<span class="badge bg-success">未使用</span>';
                    break;
                case 'used':
                    statusBadge = '<span class="badge bg-info">已使用</span>';
                    break;
                case 'disabled':
                    statusBadge = '<span class="badge bg-secondary">已禁用</span>';
                    break;
                default:
                    statusBadge = '<span class="badge bg-warning">未知</span>';
            }

            // 有效期显示
            const durationText = card.duration_days === 0 ? '永久' : `${card.duration_days}天`;

            // 硬件ID显示
            const hardwareIdDisplay = card.used_hardware_id
                ? `<span class="hardware-id-display" onclick="copyToClipboard('${card.used_hardware_id}')" title="点击复制" style="cursor: pointer;">${card.used_hardware_id.substring(0, 16)}...</span>`
                : '<span class="text-muted">-</span>';

            row.innerHTML = `
                <td><code onclick="copyToClipboard('${card.card_code}')" style="cursor: pointer;" title="点击复制">${card.card_code}</code></td>
                <td>${card.card_type}</td>
                <td>${durationText}</td>
                <td>${statusBadge}</td>
                <td><small>${card.created_at || '-'}</small></td>
                <td><small>${card.used_at || '-'}</small></td>
                <td>${hardwareIdDisplay}</td>
                <td>
                    <div class="btn-group btn-group-sm">
                        ${card.status === 'unused' ?
                            `<button class="btn btn-danger btn-sm" onclick="deleteCard(${card.id}, event)" title="删除">
                                <i class="bi bi-trash"></i>
                            </button>` : ''}
                    </div>
                </td>
            `;
            tableBody.appendChild(row);
        });

        console.log(`成功加载 ${data.cards.length} 条卡密记录`);

    } catch (error) {
        console.error('刷新卡密列表失败:', error);
        tableBody.innerHTML = '<tr><td colspan="8" class="text-center text-danger">加载失败，请重试</td></tr>';
        showAlert('获取卡密列表失败: ' + error.message, 'danger');
    }
}

// 生成卡密
async function generateCards() {
    const cardType = String(document.getElementById('cardType').value || '').trim().toUpperCase();
    const durationDays = parseInt(document.getElementById('durationDays').value);
    const quantity = parseInt(document.getElementById('quantity').value);
    const notes = String(document.getElementById('cardNotes').value || '').trim();
    const parentLicenseKey = String(document.getElementById('generateCardParentLicenseKey')?.value || '').trim().toUpperCase();

    if (!cardType || isNaN(durationDays) || durationDays < 0) {
        showAlert('请填写有效的卡密类型和有效期', 'warning');
        return;
    }

    if (!quantity || quantity < 1 || quantity > 1000) {
        showAlert('生成数量必须在1-1000之间', 'warning');
        return;
    }

    if (cardType === 'EXECUTOR' && !parentLicenseKey) {
        showAlert('请填写上级编辑器授权码', 'warning');
        return;
    }

    try {
        const requestPayload = {
            card_type: cardType,
            duration_days: durationDays,
            quantity: quantity,
            notes: notes
        };
        if (cardType === 'EXECUTOR') {
            requestPayload.parent_license_key = parentLicenseKey;
        }

        const response = await fetch('/api/admin/cards/generate', {
            method: 'POST',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestPayload)
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || '生成卡密失败');
        }

        // 关闭模态框
        const modal = bootstrap.Modal.getInstance(document.getElementById('generateCardsModal'));
        modal.hide();

        // 清空表单
        document.getElementById('generateCardsForm').reset();
        toggleExecutorParentLicenseInput();

        // 显示成功信息
        showAlert(`成功生成 ${data.cards.length} 张卡密，批次ID: ${data.batch_id}`, 'success');

        // 刷新列表
        await refreshCards();

        // 询问是否导出
        if (confirm('卡密生成成功！是否立即导出？')) {
            await exportBatch(data.batch_id);
        }

    } catch (error) {
        console.error('生成卡密失败:', error);
        showAlert('生成卡密失败: ' + error.message, 'danger');
    }
}

// 设置有效期快捷选择
function setDuration(days) {
    document.getElementById('durationDays').value = days;
}

function toggleExecutorParentLicenseInput() {
    const cardTypeSelect = document.getElementById('cardType');
    const parentGroup = document.getElementById('executorParentLicenseGroup');
    const parentInput = document.getElementById('generateCardParentLicenseKey');
    if (!cardTypeSelect || !parentGroup || !parentInput) {
        return;
    }

    const isExecutor = String(cardTypeSelect.value || '').trim().toUpperCase() === 'EXECUTOR';
    parentGroup.classList.toggle('d-none', !isExecutor);
    parentInput.required = isExecutor;
    if (!isExecutor) {
        parentInput.value = '';
    }
}

async function requestSecondaryPasswordForDeleteForCards(actionName) {
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

async function sendDeleteRequestWithSecondaryVerificationForCards(url, actionName) {
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
                'Content-Type': 'application/json'
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
        const secondaryPassword = await requestSecondaryPasswordForDeleteForCards(actionName);
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

// 删除单个卡密
async function deleteCard(cardId, event) {
    // 防止重复点击
    if (event && event.target) {
        const button = event.target.closest('button');
        if (button && button.disabled) {
            return; // 按钮已被禁用，直接返回
        }
        if (button) {
            button.disabled = true;
            button.innerHTML = '<span class="spinner-border spinner-border-sm"></span>';
        }
    }

    if (!confirm('确定要删除这张卡密吗？此操作不可恢复！')) {
        // 用户取消，恢复按钮
        if (event && event.target) {
            const button = event.target.closest('button');
            if (button) {
                button.disabled = false;
                button.innerHTML = '<i class="bi bi-trash"></i>';
            }
        }
        return;
    }

    try {
        const result = await sendDeleteRequestWithSecondaryVerificationForCards(`/api/admin/cards/${cardId}`, '删除卡密');
        if (result.cancelled) {
            if (event && event.target) {
                const button = event.target.closest('button');
                if (button) {
                    button.disabled = false;
                    button.innerHTML = '<i class="bi bi-trash"></i>';
                }
            }
            return;
        }
        const { response, data } = result;

        // 如果是404错误，说明卡密已经被删除了，直接刷新列表
        if (response.status === 404) {
            console.log('卡密已被删除(404)，刷新列表');
            showAlert('卡密不存在或已被删除', 'warning');
            await refreshCards();
            return;
        }

        if (!response.ok) {
            throw new Error(data.detail || '删除失败');
        }

        console.log(`成功删除卡密 ID=${cardId}`);
        showAlert('卡密删除成功', 'success');

        // 强制刷新整个列表
        console.log('开始刷新卡密列表...');
        await refreshCards();
        console.log('卡密列表刷新完成');

    } catch (error) {
        console.error('删除卡密失败:', error);
        showAlert('删除卡密失败: ' + error.message, 'danger');

        // 恢复按钮状态
        if (event && event.target) {
            const button = event.target.closest('button');
            if (button) {
                button.disabled = false;
                button.innerHTML = '<i class="bi bi-trash"></i>';
            }
        }
    }
}

// 显示批次管理
async function showCardBatches() {
    const batchesSection = document.getElementById('batches-section');
    const batchesTable = document.getElementById('batches-table');

    batchesSection.style.display = 'block';
    batchesTable.innerHTML = '<tr><td colspan="8" class="text-center"><div class="spinner-border"></div></td></tr>';

    try {
        // 添加时间戳防止缓存
        const timestamp = new Date().getTime();
        const response = await fetch(`/api/admin/cards/batches?_t=${timestamp}`, {
            credentials: 'include',
            cache: 'no-cache',
            headers: {
                'Cache-Control': 'no-cache, no-store, must-revalidate',
                'Pragma': 'no-cache'
            }
        });

        console.log('批次API响应状态:', response.status);

        if (!response.ok) {
            const errorText = await response.text();
            console.error('批次API错误响应:', errorText);
            throw new Error(`获取批次列表失败 (${response.status})`);
        }

        const data = await response.json();
        console.log('批次数据:', data);

        if (data.batches.length === 0) {
            batchesTable.innerHTML = '<tr><td colspan="8" class="text-center text-muted">暂无批次记录</td></tr>';
            return;
        }

        batchesTable.innerHTML = '';
        data.batches.forEach(batch => {
            const row = document.createElement('tr');
            row.setAttribute('data-batch-id', batch.batch_id); // 添加标识符

            const durationText = batch.duration_days === 0 ? '永久' : `${batch.duration_days}天`;

            row.innerHTML = `
                <td><code>${batch.batch_id}</code></td>
                <td>${batch.total}</td>
                <td><span class="badge bg-success">${batch.unused}</span></td>
                <td><span class="badge bg-info">${batch.used}</span></td>
                <td>${durationText}</td>
                <td><small>${batch.created_at}</small></td>
                <td>${batch.created_by}</td>
                <td>
                    <div class="btn-group btn-group-sm">
                        <button class="btn btn-primary btn-sm" onclick="exportBatch('${batch.batch_id}')" title="导出">
                            <i class="bi bi-download"></i>
                        </button>
                        <button class="btn btn-danger btn-sm" onclick="deleteBatch('${batch.batch_id}', event)" title="删除">
                            <i class="bi bi-trash"></i>
                        </button>
                    </div>
                </td>
            `;
            batchesTable.appendChild(row);
        });

        console.log(`成功加载 ${data.batches.length} 个批次`);

    } catch (error) {
        console.error('获取批次列表失败:', error);
        batchesTable.innerHTML = '<tr><td colspan="8" class="text-center text-danger">加载失败</td></tr>';
        showAlert('获取批次列表失败: ' + error.message, 'danger');
    }
}

// 隐藏批次管理
function hideBatches() {
    document.getElementById('batches-section').style.display = 'none';
}

// 导出批次
async function exportBatch(batchId) {
    try {
        document.getElementById('exportBatchId').value = batchId;

        // 获取导出预览
        await updateExportPreview();

        // 显示导出模态框
        const modal = new bootstrap.Modal(document.getElementById('exportCardsModal'));
        modal.show();

    } catch (error) {
        console.error('导出批次失败:', error);
        showAlert('导出批次失败: ' + error.message, 'danger');
    }
}

// 更新导出预览
async function updateExportPreview() {
    const batchId = document.getElementById('exportBatchId').value;
    const format = document.querySelector('input[name="exportFormat"]:checked').value;
    const statusFilter = document.getElementById('exportStatusFilter').value;
    const preview = document.getElementById('exportPreview');

    preview.value = '加载中...';

    try {
        const response = await fetch('/api/admin/cards/export', {
            method: 'POST',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                batch_id: batchId,
                format: format,
                status: statusFilter
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || '导出失败');
        }

        preview.value = data.content;

    } catch (error) {
        console.error('更新导出预览失败:', error);
        preview.value = '预览失败: ' + error.message;
    }
}

// 下载导出文件
function downloadExport() {
    const content = document.getElementById('exportPreview').value;
    const format = document.querySelector('input[name="exportFormat"]:checked').value;
    const batchId = document.getElementById('exportBatchId').value;

    if (!content || content === '加载中...' || content.startsWith('预览失败')) {
        showAlert('没有可导出的内容', 'warning');
        return;
    }

    // 创建Blob
    const blob = new Blob([content], { type: 'text/plain;charset=utf-8' });

    // 创建下载链接
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `cards_${batchId}_${new Date().getTime()}.${format}`;
    document.body.appendChild(a);
    a.click();

    // 清理
    document.body.removeChild(a);
    URL.revokeObjectURL(url);

    showAlert('文件下载成功', 'success');
}

// 删除批次
async function deleteBatch(batchId, event) {
    // 防止重复点击
    if (event && event.target) {
        const button = event.target.closest('button');
        if (button && button.disabled) {
            return; // 按钮已被禁用，直接返回
        }
        if (button) {
            button.disabled = true;
            const originalHtml = button.innerHTML;
            button.innerHTML = '<span class="spinner-border spinner-border-sm"></span>';
            button.dataset.originalHtml = originalHtml;
        }
    }

    if (!confirm(`确定要删除批次 ${batchId} 吗？这将删除该批次的所有卡密，此操作不可恢复！`)) {
        // 用户取消，恢复按钮
        if (event && event.target) {
            const button = event.target.closest('button');
            if (button && button.dataset.originalHtml) {
                button.disabled = false;
                button.innerHTML = button.dataset.originalHtml;
            }
        }
        return;
    }

    try {
        const result = await sendDeleteRequestWithSecondaryVerificationForCards(`/api/admin/cards/batch/${batchId}`, '删除卡密批次');
        if (result.cancelled) {
            if (event && event.target) {
                const button = event.target.closest('button');
                if (button && button.dataset.originalHtml) {
                    button.disabled = false;
                    button.innerHTML = button.dataset.originalHtml;
                }
            }
            return;
        }
        const { response, data } = result;

        // 如果是404错误，说明批次已经被删除了
        if (response.status === 404) {
            console.log('批次已被删除(404)，刷新列表');
            showAlert('批次不存在或已被删除', 'warning');
            await showCardBatches();
            await refreshCards();
            return;
        }

        if (!response.ok) {
            throw new Error(data.detail || '删除批次失败');
        }

        console.log(`成功删除批次: ${batchId}`);
        showAlert(data.message || '批次删除成功', 'success');

        // 强制刷新批次列表和卡密列表
        console.log('开始刷新批次列表和卡密列表...');
        await showCardBatches();
        await refreshCards();
        console.log('刷新完成');

    } catch (error) {
        console.error('删除批次失败:', error);
        showAlert('删除批次失败: ' + error.message, 'danger');

        // 恢复按钮状态
        if (event && event.target) {
            const button = event.target.closest('button');
            if (button && button.dataset.originalHtml) {
                button.disabled = false;
                button.innerHTML = button.dataset.originalHtml;
            }
        }
    }
}

// 过滤卡密
function filterCards() {
    // 这个功能需要重新请求API with filters
    const statusFilter = document.getElementById('cardStatusFilter')?.value;
    const batchFilter = document.getElementById('cardBatchFilter')?.value;

    // TODO: 实现带过滤的刷新
    refreshCards();
}

// 搜索卡密
function searchCards() {
    const searchTerm = document.getElementById('cardSearchInput')?.value.toLowerCase();
    const rows = document.querySelectorAll('#cards-table tr');

    rows.forEach(row => {
        const cardCode = row.querySelector('code')?.textContent.toLowerCase();
        if (cardCode && cardCode.includes(searchTerm)) {
            row.style.display = '';
        } else if (cardCode) {
            row.style.display = 'none';
        }
    });
}

// 复制到剪贴板
function copyToClipboard(text) {
    if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(text).then(() => {
            showAlert('已复制到剪贴板', 'success');
        });
    } else {
        // 降级方案
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
            showAlert('已复制到剪贴板', 'success');
        } catch (err) {
            console.error('复制失败:', err);
        }
        textArea.remove();
    }
}

// 监听导出格式和状态变化
document.addEventListener('DOMContentLoaded', function() {
    const cardTypeSelect = document.getElementById('cardType');
    if (cardTypeSelect) {
        cardTypeSelect.addEventListener('change', toggleExecutorParentLicenseInput);
    }
    const parentInput = document.getElementById('generateCardParentLicenseKey');
    if (parentInput) {
        parentInput.addEventListener('input', () => {
            parentInput.value = parentInput.value.toUpperCase().replace(/\s+/g, '');
        });
    }
    toggleExecutorParentLicenseInput();

    // 导出格式变化时更新预览
    document.querySelectorAll('input[name="exportFormat"]').forEach(radio => {
        radio.addEventListener('change', updateExportPreview);
    });

    // 导出状态过滤变化时更新预览
    const exportStatusFilter = document.getElementById('exportStatusFilter');
    if (exportStatusFilter) {
        exportStatusFilter.addEventListener('change', updateExportPreview);
    }
});
