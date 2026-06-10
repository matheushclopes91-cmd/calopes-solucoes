import React, { useEffect, useRef, useState } from 'react';
import { createChart } from 'lightweight-charts';

export default function ChartD1W1({ pair }) {
  const chartContainerRef = useRef(null);
  const chartRef = useRef(null);
  const [timeframe, setTimeframe] = useState('D1');

  useEffect(() => {
    if (!chartContainerRef.current) return;

    // Create chart
    const chart = createChart(chartContainerRef.current, {
      layout: {
        textColor: '#d1d5db',
        background: { type: 'solid', color: '#111827' },
      },
      width: chartContainerRef.current.clientWidth,
      height: 400,
      timeScale: {
        timeVisible: true,
        secondsVisible: false,
      },
      grid: {
        vertLines: { color: '#2d3748' },
        horzLines: { color: '#2d3748' },
      },
    });

    chartRef.current = chart;

    // Add candlestick series
    const candlestickSeries = chart.addCandlestickSeries({
      upColor: '#10b981',
      downColor: '#ef4444',
      borderDownColor: '#ef4444',
      borderUpColor: '#10b981',
      wickDownColor: '#ef4444',
      wickUpColor: '#10b981',
    });

    // Add EMA indicators
    const ema50Series = chart.addLineSeries({
      color: '#3b82f6',
      lineWidth: 2,
      title: 'EMA 50',
    });

    const ema200Series = chart.addLineSeries({
      color: '#f59e0b',
      lineWidth: 2,
      title: 'EMA 200',
    });

    // Generate sample data (replace with real API call)
    const generateSampleData = () => {
      const now = Date.now();
      const data = [];
      const emaData50 = [];
      const emaData200 = [];

      let price = 1.0800;
      for (let i = 100; i >= 0; i--) {
        const time = (now - i * 86400000) / 1000; // Daily candles
        const open = price;
        const close = price + (Math.random() - 0.5) * 0.002;
        const high = Math.max(open, close) + Math.random() * 0.001;
        const low = Math.min(open, close) - Math.random() * 0.001;

        data.push({
          time,
          open: parseFloat(open.toFixed(4)),
          high: parseFloat(high.toFixed(4)),
          low: parseFloat(low.toFixed(4)),
          close: parseFloat(close.toFixed(4)),
        });

        // Simple EMA calculation (for demo)
        const ema50Val = price + (Math.random() - 0.5) * 0.001;
        const ema200Val = price - (Math.random() - 0.5) * 0.001;

        emaData50.push({ time, value: parseFloat(ema50Val.toFixed(4)) });
        emaData200.push({ time, value: parseFloat(ema200Val.toFixed(4)) });

        price = close;
      }

      return { data, emaData50, emaData200 };
    };

    const { data, emaData50, emaData200 } = generateSampleData();

    candlestickSeries.setData(data);
    ema50Series.setData(emaData50);
    ema200Series.setData(emaData200);

    // Fit content
    chart.timeScale().fitContent();

    // Handle resize
    const handleResize = () => {
      if (chartContainerRef.current) {
        chart.applyOptions({
          width: chartContainerRef.current.clientWidth,
        });
      }
    };

    window.addEventListener('resize', handleResize);

    return () => {
      window.removeEventListener('resize', handleResize);
      chart.remove();
    };
  }, [pair, timeframe]);

  return (
    <div className="bg-gray-800 rounded-lg border border-gray-700 p-4">
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-xl font-bold">{pair} - Technical Analysis</h2>
        <div className="flex gap-2">
          {['D1', 'W1'].map(tf => (
            <button
              key={tf}
              onClick={() => setTimeframe(tf)}
              className={`px-3 py-1 rounded text-sm transition ${
                timeframe === tf
                  ? 'bg-blue-600 text-white'
                  : 'bg-gray-700 text-gray-300 hover:bg-gray-600'
              }`}
            >
              {tf}
            </button>
          ))}
        </div>
      </div>

      <div
        ref={chartContainerRef}
        className="w-full rounded border border-gray-700"
        style={{ minHeight: '400px' }}
      />

      {/* Legend */}
      <div className="mt-4 flex gap-6 text-sm">
        <div className="flex items-center gap-2">
          <div className="w-3 h-3 bg-green-500"></div>
          <span>Up Candles</span>
        </div>
        <div className="flex items-center gap-2">
          <div className="w-3 h-3 bg-red-500"></div>
          <span>Down Candles</span>
        </div>
        <div className="flex items-center gap-2">
          <div className="w-1 h-4 bg-blue-500"></div>
          <span>EMA 50</span>
        </div>
        <div className="flex items-center gap-2">
          <div className="w-1 h-4 bg-amber-500"></div>
          <span>EMA 200</span>
        </div>
      </div>
    </div>
  );
}
