import React, { useState, useEffect } from 'react';
import ChartD1W1 from './ChartD1W1';
import OpportunitiesList from './OpportunitiesList';
import OperationHistory from './OperationHistory';
import StrategyMetrics from './StrategyMetrics';

export default function Dashboard() {
  const [selectedPair, setSelectedPair] = useState('EUR_USD');
  const [opportunities, setOpportunities] = useState([]);
  const [operationHistory, setOperationHistory] = useState([]);
  const [metrics, setMetrics] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const pairs = [
    'EUR_USD', 'GBP_USD', 'USD_JPY', 'USD_CHF', 'AUD_USD',
    'USD_CAD', 'NZD_USD', 'EUR_GBP', 'EUR_JPY', 'EUR_CHF'
  ];

  useEffect(() => {
    fetchData();
    const interval = setInterval(fetchData, 60000); // Atualizar a cada minuto
    return () => clearInterval(interval);
  }, [selectedPair]);

  const fetchData = async () => {
    try {
      setLoading(true);

      // Fetch opportunities
      const oppRes = await fetch(`http://localhost:8000/api/opportunities?pair=${selectedPair}`);
      if (oppRes.ok) {
        const oppData = await oppRes.json();
        setOpportunities(oppData.signals || []);
      }

      // Fetch operation history
      const histRes = await fetch(`http://localhost:8000/api/operations?pair=${selectedPair}`);
      if (histRes.ok) {
        const histData = await histRes.json();
        setOperationHistory(histData.operations || []);
      }

      // Fetch metrics
      const metRes = await fetch(`http://localhost:8000/api/metrics?pair=${selectedPair}`);
      if (metRes.ok) {
        const metData = await metRes.json();
        setMetrics(metData);
      }

      setError(null);
    } catch (err) {
      setError(err.message);
      console.error('Error fetching data:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-900 text-white">
      {/* Header */}
      <header className="bg-gray-800 border-b border-gray-700 p-4">
        <div className="max-w-7xl mx-auto">
          <h1 className="text-3xl font-bold mb-4">📊 Forex Trading Dashboard</h1>

          {/* Pair Selector */}
          <div className="flex gap-2 flex-wrap">
            {pairs.map(pair => (
              <button
                key={pair}
                onClick={() => setSelectedPair(pair)}
                className={`px-4 py-2 rounded transition ${
                  selectedPair === pair
                    ? 'bg-blue-600 text-white'
                    : 'bg-gray-700 text-gray-300 hover:bg-gray-600'
                }`}
              >
                {pair}
              </button>
            ))}
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto p-4 space-y-6">
        {error && (
          <div className="bg-red-900 border border-red-700 text-red-100 p-4 rounded">
            ⚠️ Error: {error}
          </div>
        )}

        {loading && (
          <div className="bg-gray-800 p-8 rounded text-center">
            <p className="text-gray-400">Loading data...</p>
          </div>
        )}

        {!loading && (
          <>
            {/* Charts Row */}
            <div className="grid grid-cols-1 lg:grid-cols-3 gap-4">
              <div className="lg:col-span-2">
                <ChartD1W1 pair={selectedPair} />
              </div>
              <div>
                <StrategyMetrics pair={selectedPair} metrics={metrics} />
              </div>
            </div>

            {/* Opportunities Row */}
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
              <OpportunitiesList pair={selectedPair} opportunities={opportunities} />
              <OperationHistory pair={selectedPair} operations={operationHistory} />
            </div>
          </>
        )}
      </main>

      {/* Footer */}
      <footer className="bg-gray-800 border-t border-gray-700 p-4 mt-8">
        <div className="max-w-7xl mx-auto text-center text-gray-400 text-sm">
          <p>Last updated: {new Date().toLocaleTimeString()}</p>
          <p>Analysis: Saturday 14:00 CET | Execution: Sunday 17:00 CET</p>
        </div>
      </footer>
    </div>
  );
}
