import './App.css';
import { useState } from 'react';

import fileIcon from './images/file-icon.png';
import runIcon from './images/run-icon.png'
import mainIcon from './images/main-icon.png'
import phraseIcon from './images/phrase-icon.png'
import wordIcon from './images/word-icon.png'
import gaugeIcon from './images/gauge-icon.png'

function App() {
  const [file1, setFile1] = useState(null);
  const [file2, setFile2] = useState(null);
  const [hasRun, setHasRun] = useState(false)
  const [result, setResult] = useState({
    score: "N/A",
    label: "N/A", 
    longest_phrase: "N/A",
    most_common: "N/A"
  });

  const getLabelColor = (label) => {
      if (label === 'No Similarity') return '#15803D'
      if (label === 'Very Low Similarity') return '#22C55E'
      if (label === 'Low Similarity') return '#a0ff0f'
      if (label === 'Moderate Similarity') return '#F59E0B'
      if (label === 'High Similarity') return '#F97316'
      if (label === 'Very High Similarity') return '#DC2626'
      return '#000000'
    };

  const handleCompare = async () => {
    // Stops user sending empty requests by checking if both files are present
    if (!file1 || !file2) {
      alert('Missing files')
      return;
    }

    // FormData is an object to send data (files) to backend
    const formData = new FormData();
    formData.append("file1", file1);
    formData.append("file2", file2);

    // Sends request to run compare() function
    const response = await fetch("http://127.0.0.1:5000/compare", {
      method: "POST",
      body: formData
    });

    const data = await response.json(); // Converts JSON to JS object
    setResult(data); // Re-renders with data from backend

    setHasRun(true);
  }

  return (
    <div className='app-container'>
      <div>
        <div className='title-row'>
          <img src={mainIcon} alt="File" className='main-icon' />
          <p className='title'>Plagiarism Detector Tool</p>
        </div>

        <div className='input-box'>
          <div className='file-upload'>
            <div className='file-name'>
              <p>Document 1</p>

              <div className='file-row'>
                <img src={fileIcon} alt="File" className='file-icon' />
                <span className='file-text'>{file1 ? file1.name : "No file chosen"}</span>
              </div>
            </div>

            <label htmlFor='file1' className='browse-button'>Browse</label>

            <input id='file1' type='file' className='hidden-file-input' onChange={(e) => setFile1(e.target.files[0])}/>
          </div>

          <div className='file-upload'>
            <div className='file-name'>
              <p>Document 2</p>

              <div className='file-row'>
                <img src={fileIcon} alt="File" className='file-icon' />
                <span className='file-text'>{file2 ? file2.name : "No file chosen"}</span>
              </div>
            </div>

            <label htmlFor='file2' className='browse-button'>Browse</label>

            <input id='file2' type='file' className='hidden-file-input' onChange={(e) => setFile2(e.target.files[0])}/>
          </div>

          <button onClick={handleCompare} className='run-button'>
            <img src={runIcon} alt="" className='run-icon' />
            Run Analysis
          </button>
        </div>

          <div className='results-box'>
            <p className='results-text'>Results Summary</p>

            <div className='results-grid'>
              <div className='results-card'>
                <p className='similarity-title'>Jaccard Similarity Score</p>
                <p className='similarity-value'>{result.score}</p>
              </div>

              <div className='results-card'>
                <p className='similarity-level-title'>Similarity Level</p>
                <p className='similarity-level-value' style={{color: getLabelColor(result.label)}}>{result.label}</p>
              </div>

              <div className='results-card'>
                <img src={gaugeIcon} alt="icon" className='guage-icon'></img>
              </div>
            </div>
          </div>
          
          <div className='insights-box'>
            <p className='insights-text'>Key Insights</p>

            <div className='insights-grid'>
              <div className='longest-phrase-grid'>
                <img src={phraseIcon} alt="icon" className='insight-icon' />

                <div className='insight-content'>
                  <p className='longest-phrase-text'>Longest Matching Phrase</p>
                  <p className='longest-phrase-result'>{result.longest_phrase}</p>
                </div>
              </div>

              <div className='common-phrase-grid'>
                <img src={wordIcon} alt="icon" className='insight-icon' />

                <div className='insight-content'>
                  <p className='common-phrase-text'>Most Common Word</p>
                  <p className='common-phrase-result'>{result.most_common}</p>
                </div>
              </div>
            </div>
          </div>

          <div
            className={`status-message ${hasRun ? "status-done" : "status-empty"}`}>
            
            {!hasRun
              ? "No analysis yet — upload files and run analysis"
              : "Analysis complete ✓"}
          </div>
      </div>
    </div>
  );
}

export default App;