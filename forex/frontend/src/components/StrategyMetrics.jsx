import React from 'react';

export default function StrategyMetrics({ pair, metrics }) {
  const getMeterColor = (value, target, isPercent = false) => {
    if (value === null || value === undefined || value === 'N/A') {
      return 'bg-gray-600';
    }

    const numValue = typeof value === 'string' ? parseFloat(value) : value;
    const percentage = isPercent ? numValue : numValue;

    if (percentage >= target) return 'bg-green-600';
    if (percentage >= target * 0.7) return 'bg-yellow-600';
    return 'bg-red-600';
  };

  const MetricCard = ({ title, value, target, unit = '', isPercent = false }) => {
    const displayValue =
      typeof value === 'number' ? value.toFixed(2) : value || 'N/A';

    return (
      <div className="bg-gray-700 rounded p-3">
        <p className="text-gray-400 text-xs">{title}</p>
        <p className="text-2xl font-bold mt-1">{displayValue}{unit}</p>
        {target && (
          <>
            <p className="text-xs text-gray-500 mt-1">Target: {target}{unit}</p>
            <div className="w-full bg-gray-600 rounded-full h-1.5 mt-2">
              <div
                className={`h-1.5 rounded-full ${getMeterColor(
                  displayValue,
                  target,
                  isPercent
                )}`}
                style={{
                  width: `${Math.min(
                    ((typeof displayValue === 'number'
                      ? displayValue
                      : parseFloat(displayValue)) /
                      target) *
                      100,
                    100
                  )}%`,
                }}
              ></div>
            </div>
          </>
        )}
      </div>
    );
  };

  return (
    <div className="bg-gray-800 rounded-lg border border-gray-700 p-4">
      <h2 className="text-xl font-bold mb-4">📊 Strategy Metrics</h2>

      {!metrics ? (
        <div className="text-gray-400 text-center py-8">
          <p>Loading metrics...</p>
        </div>
      ) : (
        <div className="space-y-3">
          <MetricCard
            title="Sharpe Ratio"
            value={metrics.sharpe_ratio}
            target={1.0}
            unit=""
          />
          <MetricCard
            title="Win Rate"
            value={metrics.win_rate}
            target={50}
            unit="%"
            isPercent={true}
          />
          <MetricCard
            title="Profit Factor"
            value={metrics.profit_factor}
            target={1.5}
            unit=""
          />
          <MetricCard
            title="Max Drawdown"
            value={metrics.max_drawdown}
            target={20}
            unit="%"
            isPercent={true}
          />

          <div className="border-t border-gray-600 pt-3 mt-3">
            <p className="text-gray-400 text-xs mb-2">Quick Stats</p>
            <div className="grid grid-cols-2 gap-2 text-sm">
              <div>
                <p className="text-gray-500">Total Return</p>
                <p className="font-bold text-green-400">
                  {metrics.return_pct || 'N/A'}%
                </p>
              </div>
              <div>
                <p className="text-gray-500">Trades</p>
                <p className="font-bold">{metrics.trades || 0}</p>
              </div>
              <div>
                <p className="text-gray-500">Wins</p>
                <p className="font-bold text-green-400">{metrics.wins || 0}</p>
              </div>
              <div>
                <p className="text-gray-500">Losses</p>
                <p className="font-bold text-red-400">{metrics.losses || 0}</p>
              </div>
            </div>
          </div>

          {/* Status Badge */}
          <div className="mt-4 p-3 rounded bg-gray-700 border border-gray-600">
            <p className="text-xs text-gray-400 mb-1">Strategy Status</p>
            {metrics.sharpe_ratio >= 1.0 &&
            metrics.win_rate >= 50 &&
            metrics.profit_factor >= 1.5 ? (
              <p className="text-green-400 font-bold">
                ✅ Ready for Trading
              </p>
            ) : (
              <p className="text-yellow-400 font-bold">
                ⚠️ Needs Optimization
              </p>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
