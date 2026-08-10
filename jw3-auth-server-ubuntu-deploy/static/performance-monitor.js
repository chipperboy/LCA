/**
 * 性能监控脚本
 * 用于监控页面加载性能和用户体验指标
 */

class PerformanceMonitor {
    constructor() {
        this.metrics = {};
        this.startTime = performance.now();
        this.init();
    }

    init() {
        // 监听页面加载完成
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => this.onDOMContentLoaded());
        } else {
            this.onDOMContentLoaded();
        }

        // 监听页面完全加载
        window.addEventListener('load', () => this.onLoad());

        // 监听页面可见性变化
        document.addEventListener('visibilitychange', () => this.onVisibilityChange());
    }

    onDOMContentLoaded() {
        this.metrics.domContentLoaded = performance.now() - this.startTime;
        console.log(`📊 DOM内容加载完成: ${this.metrics.domContentLoaded.toFixed(2)}ms`);
    }

    onLoad() {
        this.metrics.windowLoad = performance.now() - this.startTime;
        console.log(`📊 页面完全加载: ${this.metrics.windowLoad.toFixed(2)}ms`);
        
        // 获取详细的性能指标
        this.collectDetailedMetrics();
        this.reportMetrics();
    }

    onVisibilityChange() {
        if (document.hidden) {
            console.log('📊 页面变为不可见');
        } else {
            console.log('📊 页面变为可见');
        }
    }

    collectDetailedMetrics() {
        // 获取导航时间
        const navigation = performance.getEntriesByType('navigation')[0];
        if (navigation) {
            this.metrics.navigation = {
                dns: navigation.domainLookupEnd - navigation.domainLookupStart,
                tcp: navigation.connectEnd - navigation.connectStart,
                ssl: navigation.secureConnectionStart > 0 ? navigation.connectEnd - navigation.secureConnectionStart : 0,
                ttfb: navigation.responseStart - navigation.requestStart,
                download: navigation.responseEnd - navigation.responseStart,
                domParse: navigation.domContentLoadedEventEnd - navigation.domContentLoadedEventStart,
                totalLoad: navigation.loadEventEnd - navigation.loadEventStart
            };
        }

        // 获取资源加载时间
        const resources = performance.getEntriesByType('resource');
        this.metrics.resources = resources.map(resource => ({
            name: resource.name.split('/').pop(),
            type: this.getResourceType(resource.name),
            duration: resource.duration,
            size: resource.transferSize || 0
        }));

        // 获取内存使用情况（如果支持）
        if (performance.memory) {
            this.metrics.memory = {
                used: performance.memory.usedJSHeapSize,
                total: performance.memory.totalJSHeapSize,
                limit: performance.memory.jsHeapSizeLimit
            };
        }

        // 获取Web Vitals指标（如果支持）
        this.collectWebVitals();
    }

    getResourceType(url) {
        if (url.includes('.css')) return 'CSS';
        if (url.includes('.js')) return 'JavaScript';
        if (url.includes('.woff') || url.includes('.woff2')) return 'Font';
        if (url.includes('.png') || url.includes('.jpg') || url.includes('.svg')) return 'Image';
        return 'Other';
    }

    collectWebVitals() {
        // 尝试获取LCP (Largest Contentful Paint)
        try {
            new PerformanceObserver((entryList) => {
                const entries = entryList.getEntries();
                const lastEntry = entries[entries.length - 1];
                this.metrics.lcp = lastEntry.startTime;
                console.log(`📊 LCP (最大内容绘制): ${this.metrics.lcp.toFixed(2)}ms`);
            }).observe({ entryTypes: ['largest-contentful-paint'] });
        } catch (e) {
            console.log('📊 LCP 不支持');
        }

        // 尝试获取FCP (First Contentful Paint)
        try {
            new PerformanceObserver((entryList) => {
                const entries = entryList.getEntries();
                const firstEntry = entries[0];
                this.metrics.fcp = firstEntry.startTime;
                console.log(`📊 FCP (首次内容绘制): ${this.metrics.fcp.toFixed(2)}ms`);
            }).observe({ entryTypes: ['paint'] });
        } catch (e) {
            console.log('📊 FCP 不支持');
        }

        // 尝试获取CLS (Cumulative Layout Shift)
        try {
            let clsValue = 0;
            new PerformanceObserver((entryList) => {
                for (const entry of entryList.getEntries()) {
                    if (!entry.hadRecentInput) {
                        clsValue += entry.value;
                    }
                }
                this.metrics.cls = clsValue;
                console.log(`📊 CLS (累积布局偏移): ${this.metrics.cls.toFixed(4)}`);
            }).observe({ entryTypes: ['layout-shift'] });
        } catch (e) {
            console.log('📊 CLS 不支持');
        }
    }

    reportMetrics() {
        console.group('📊 性能监控报告');
        
        // 基础指标
        console.log(`DOM加载时间: ${this.metrics.domContentLoaded?.toFixed(2) || 'N/A'}ms`);
        console.log(`页面加载时间: ${this.metrics.windowLoad?.toFixed(2) || 'N/A'}ms`);
        
        // 导航指标
        if (this.metrics.navigation) {
            console.group('🌐 网络指标');
            console.log(`DNS查询: ${this.metrics.navigation.dns.toFixed(2)}ms`);
            console.log(`TCP连接: ${this.metrics.navigation.tcp.toFixed(2)}ms`);
            console.log(`SSL握手: ${this.metrics.navigation.ssl.toFixed(2)}ms`);
            console.log(`首字节时间: ${this.metrics.navigation.ttfb.toFixed(2)}ms`);
            console.log(`下载时间: ${this.metrics.navigation.download.toFixed(2)}ms`);
            console.groupEnd();
        }

        // 资源指标
        if (this.metrics.resources) {
            console.group('📦 资源加载');
            const resourcesByType = this.metrics.resources.reduce((acc, resource) => {
                if (!acc[resource.type]) acc[resource.type] = [];
                acc[resource.type].push(resource);
                return acc;
            }, {});

            Object.entries(resourcesByType).forEach(([type, resources]) => {
                const totalDuration = resources.reduce((sum, r) => sum + r.duration, 0);
                const totalSize = resources.reduce((sum, r) => sum + r.size, 0);
                console.log(`${type}: ${resources.length}个文件, ${totalDuration.toFixed(2)}ms, ${(totalSize/1024).toFixed(2)}KB`);
            });
            console.groupEnd();
        }

        // 内存指标
        if (this.metrics.memory) {
            console.group('💾 内存使用');
            console.log(`已使用: ${(this.metrics.memory.used / 1024 / 1024).toFixed(2)}MB`);
            console.log(`总计: ${(this.metrics.memory.total / 1024 / 1024).toFixed(2)}MB`);
            console.log(`限制: ${(this.metrics.memory.limit / 1024 / 1024).toFixed(2)}MB`);
            console.groupEnd();
        }

        // Web Vitals
        console.group('🎯 Web Vitals');
        console.log(`FCP: ${this.metrics.fcp?.toFixed(2) || 'N/A'}ms`);
        console.log(`LCP: ${this.metrics.lcp?.toFixed(2) || 'N/A'}ms`);
        console.log(`CLS: ${this.metrics.cls?.toFixed(4) || 'N/A'}`);
        console.groupEnd();

        console.groupEnd();

        // 性能评分
        this.calculatePerformanceScore();
    }

    calculatePerformanceScore() {
        let score = 100;
        let feedback = [];

        // FCP评分
        if (this.metrics.fcp) {
            if (this.metrics.fcp > 3000) {
                score -= 20;
                feedback.push('FCP过慢 (>3s)');
            } else if (this.metrics.fcp > 1800) {
                score -= 10;
                feedback.push('FCP较慢 (>1.8s)');
            }
        }

        // LCP评分
        if (this.metrics.lcp) {
            if (this.metrics.lcp > 4000) {
                score -= 25;
                feedback.push('LCP过慢 (>4s)');
            } else if (this.metrics.lcp > 2500) {
                score -= 15;
                feedback.push('LCP较慢 (>2.5s)');
            }
        }

        // CLS评分
        if (this.metrics.cls) {
            if (this.metrics.cls > 0.25) {
                score -= 20;
                feedback.push('CLS过高 (>0.25)');
            } else if (this.metrics.cls > 0.1) {
                score -= 10;
                feedback.push('CLS较高 (>0.1)');
            }
        }

        // 页面加载时间评分
        if (this.metrics.windowLoad) {
            if (this.metrics.windowLoad > 5000) {
                score -= 15;
                feedback.push('页面加载过慢 (>5s)');
            } else if (this.metrics.windowLoad > 3000) {
                score -= 8;
                feedback.push('页面加载较慢 (>3s)');
            }
        }

        console.group('🏆 性能评分');
        console.log(`总分: ${Math.max(0, score)}/100`);
        if (feedback.length > 0) {
            console.log('改进建议:');
            feedback.forEach(item => console.log(`- ${item}`));
        } else {
            console.log('🎉 性能表现优秀！');
        }
        console.groupEnd();
    }

    // 手动触发性能报告
    getReport() {
        return {
            timestamp: new Date().toISOString(),
            metrics: this.metrics,
            userAgent: navigator.userAgent,
            url: window.location.href
        };
    }
}

// 自动启动性能监控
if (typeof window !== 'undefined') {
    window.performanceMonitor = new PerformanceMonitor();
    
    // 添加到全局对象，方便调试
    window.getPerformanceReport = () => window.performanceMonitor.getReport();
}
