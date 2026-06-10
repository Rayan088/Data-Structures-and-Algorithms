import './App.css';
import { useState } from 'react';

function App() {
  const [file1, setFile1] = useState(null);
  const [file2, setFile2] = useState(null);
  const [result, setResult] = useState({
    score: "N/A",
    label: "N/A", 
    longest_phrase: "N/A",
    most_common: "N/A"
  });

  const handleCompare = async () => {
    if (!file1 || !file2) {
      alert('Missing files')
      return;
    }

    const formData = new FormData();
    formData.append("file1", file1);
    formData.append("file2", file2);

    const response = await fetch("http://127.0.0.1:5000/compare", {
      method: "POST",
      body: formData
    });

    const data = await response.json();
    setResult(data);
  }

  return (
    <div>
      <p className='title'>Plagiarism Detector Tool</p>

      <div className='input-box'>
        <input type='file' onChange={(e) => setFile1(e.target.files[0])} className='input1' />
        <input type="file" onChange={(e) => setFile2(e.target.files[0])} className='input2' />
        
        <button onClick={handleCompare} className='run-button'>Run Analysis</button>
      </div>

        <div className='results-box'>
          <p className='results-text'>Results Summary</p>

          <div className='results-grid'>
            <div className='result-card'>
              <p className='similarity-title'>Jaccard Similarity Score</p>
              <p className='similarity-value'>{result.score}</p>
            </div>

            <div className='result-card'>
              <p className='similarity-level-title'>Similarity Level</p>
              <p className='similarity-level-value'>{result.label}</p>
            </div>

            <div className='result-card'>
              <p className='result-value'>IMAGE HERE</p>
            </div>
          </div>
        </div>
        
        <div className='insights-box'>
          <p className='insights-text'>Key Insights</p>

          <div className='insights-grid'>
            <div className='longest-phrase-grid'>
              <p className='longest-phrase-text'>Longest Matching Phrase</p>
              <p className='longest-phrase-result'>{result.longest_phrase}</p>
            </div>

            <div className='common-phrase-grid'>
              <p className='common-phrase-text'>Most Common Word</p>
              <p className='common-phrase-result'>{result.most_common}</p>
            </div>
          </div>
        </div>
    </div>
  );
}

export default App;