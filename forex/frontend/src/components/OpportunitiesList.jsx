import React from 'react';

export default function OpportunitiesList({ pair, opportunities }) {
  const formatPrice = (price) => {
    return typeof price === 'number' ? price.toFixed(5) : price;
  };

  const getDirectionColor = (direction) => {
    return direction === 'LONG' ? 'text-green-400' : 'text-red-400';
  };

  const getConfidenceColor = (confidence) => {
    if (confidence >= 0.8) return 'bg-green-900 text-green-200';
    if (confidence >= 0.6) return 'bg-yellow-900 text-yellow-200';
    return 'bg-orange-900 text-orange-200';
  };

  return (
    <div className="bg-gray-800 rounded-lg border border-gray-700 p-4">
      <h2 className="text-xl font-bold mb-4">
        📈 Trading Opportunities
      </h2>

      {opportunities.length === 0 ? (
        <div className="text-gray-400 text-center py-8">
          <p>No opportunities for {pair} at the moment</p>
          <p className="text-sm mt-2">Next analysis: Saturday 14:00 CET</p>
        </div>
      ) : (
        <div className="space-y-3">
          {opportunities.map((opp, idx) => (
            <div
              key={idx}
              className="bg-gray-700 rounded p-4 border-l-4"
              style={{
                borderLeftColor: opp.direction === 'LONG' ? '#10b981' : '#ef4444',
              }}
            >
              <div className="flex justify-between items-start mb-2">
                <div>
                  <span className={`text-lg font-bold ${getDirectionColor(opp.direction)}`}>
                    {opp.direction}
                  </span>
                  <span className="text-gray-400 text-sm ml-2">
                    {opp.strategy || 'EMA Crossover'}
                  </span>
                </div>
                <span className={`text-xs px-2 py-1 rounded ${getConfidenceColor(opp.confidence)}`}>
                  {(opp.confidence * 100).toFixed(0)}% confidence
                </span>
              </div>

              <div className="grid grid-cols-2 gap-3 text-sm">
                <div>
                  <p className="text-gray-400">Entry</p>
                  <p className="text-white font-mono text-lg">
                    {formatPrice(opp.entry_price)}
                  </p>
                </div>
                <div>
                  <p className="text-gray-400">Risk</p>
                  <p className="text-white font-mono text-lg">
                    {formatPrice(opp.risk)}
                  </p>
                </div>
                <div>
                  <p className="text-gray-400">Stop Loss</p>
                  <p className="text-red-400 font-mono">
                    {formatPrice(opp.stop_loss)}
                  </p>
                </div>
                <div>
                  <p className="text-gray-400">Take Profit</p>
                  <p className="text-green-400 font-mono">
                    {formatPrice(opp.take_profit)}
                  </p>
                </div>
              </div>

              {opp.confirming_strategies && opp.confirming_strategies.length > 0 && (
                <div className="mt-3 pt-3 border-t border-gray-600">
                  <p className="text-xs text-yellow-400">
                    ⭐ Confluence: {opp.confirming_strategies.join(' + ')}
                  </p>
                </div>
              )}

              <div className="mt-3 flex gap-2">
                <button className="flex-1 bg-green-600 hover:bg-green-700 text-white py-2 rounded text-sm font-medium transition">
                  Execute
                </button>
                <button className="flex-1 bg-gray-600 hover:bg-gray-500 text-white py-2 rounded text-sm transition">
                  Details
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
