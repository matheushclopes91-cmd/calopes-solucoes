import React from 'react';

export default function OperationHistory({ pair, operations }) {
  const formatPrice = (price) => {
    return typeof price === 'number' ? price.toFixed(5) : price;
  };

  const getStatusColor = (status) => {
    if (status === 'CLOSED_WIN') return 'text-green-400';
    if (status === 'CLOSED_LOSS') return 'text-red-400';
    if (status === 'OPEN') return 'text-blue-400';
    return 'text-gray-400';
  };

  const getStatusBg = (status) => {
    if (status === 'CLOSED_WIN') return 'bg-green-900';
    if (status === 'CLOSED_LOSS') return 'bg-red-900';
    if (status === 'OPEN') return 'bg-blue-900';
    return 'bg-gray-900';
  };

  const calculatePnL = (op) => {
    if (op.status === 'OPEN') return null;
    if (op.direction === 'LONG') {
      return ((op.exit_price - op.entry_price) / op.entry_price * 100).toFixed(2);
    } else {
      return ((op.entry_price - op.exit_price) / op.entry_price * 100).toFixed(2);
    }
  };

  return (
    <div className="bg-gray-800 rounded-lg border border-gray-700 p-4">
      <h2 className="text-xl font-bold mb-4">📋 Operation History</h2>

      {operations.length === 0 ? (
        <div className="text-gray-400 text-center py-8">
          <p>No operations for {pair} yet</p>
          <p className="text-sm mt-2">Operations will appear after execution</p>
        </div>
      ) : (
        <div className="space-y-2 max-h-96 overflow-y-auto">
          {operations.map((op) => {
            const pnl = calculatePnL(op);
            return (
              <div
                key={op.id}
                className={`rounded p-3 text-sm border-l-4 ${getStatusBg(op.status)}`}
                style={{
                  borderLeftColor:
                    op.direction === 'LONG' ? '#10b981' : '#ef4444',
                }}
              >
                <div className="flex justify-between items-start mb-2">
                  <div>
                    <span className="font-bold">
                      {op.direction}
                    </span>
                    <span className={`ml-2 ${getStatusColor(op.status)}`}>
                      {op.status.replace('_', ' ')}
                    </span>
                  </div>
                  {pnl && (
                    <span
                      className={`font-bold ${
                        parseFloat(pnl) >= 0
                          ? 'text-green-400'
                          : 'text-red-400'
                      }`}
                    >
                      {parseFloat(pnl) >= 0 ? '+' : ''}{pnl}%
                    </span>
                  )}
                </div>

                <div className="grid grid-cols-2 gap-2 text-xs text-gray-300">
                  <div>
                    <span className="text-gray-400">Entry:</span>{' '}
                    <span className="font-mono">
                      {formatPrice(op.entry_price)}
                    </span>
                  </div>
                  <div>
                    <span className="text-gray-400">Exit:</span>{' '}
                    <span className="font-mono">
                      {formatPrice(op.exit_price || '-')}
                    </span>
                  </div>
                  <div>
                    <span className="text-gray-400">Entry:</span>{' '}
                    <span className="font-mono text-xs">
                      {new Date(op.entry_time).toLocaleDateString()}
                    </span>
                  </div>
                  <div>
                    <span className="text-gray-400">Exit:</span>{' '}
                    <span className="font-mono text-xs">
                      {op.exit_time
                        ? new Date(op.exit_time).toLocaleDateString()
                        : '-'}
                    </span>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      )}

      {/* Summary Stats */}
      {operations.length > 0 && (
        <div className="mt-4 pt-4 border-t border-gray-700">
          <div className="grid grid-cols-3 gap-2 text-xs">
            <div>
              <p className="text-gray-400">Total Trades</p>
              <p className="text-lg font-bold">{operations.length}</p>
            </div>
            <div>
              <p className="text-gray-400">Win Rate</p>
              <p className="text-lg font-bold text-green-400">
                {(
                  (operations.filter(
                    (op) => op.status === 'CLOSED_WIN'
                  ).length /
                    operations.filter((op) => op.status.startsWith('CLOSED'))
                      .length) *
                  100
                ).toFixed(0)}
                %
              </p>
            </div>
            <div>
              <p className="text-gray-400">Open Trades</p>
              <p className="text-lg font-bold text-blue-400">
                {operations.filter((op) => op.status === 'OPEN').length}
              </p>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
