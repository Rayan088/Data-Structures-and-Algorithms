import './App.css';
import { useState } from 'react';

function App() {
  const [file1, setFile1] = useState(null);
  const [file2, setFile2] = useState(null);
  const [result, setResult] = useState(null);

  const handleCompare = async () => {
    if (!file1 || !file2) {
      alert('Upload both files');
      return;
    }

    const formData = new FormData();
    formData.append("file1", file1);
    formData.append("file2", file2);

    const response = await fetch("http://localhost:5000/compare", {
      method: "POST",
      body: formData
    });

    const data = await response.json();
    setResult(data);
  }

  return (
    <div>
      <p className='title'>Plagiarism Detector</p>

      <div className='input-box'>
        <input type='file' onChange={(e) => setFile1(e.target.files[0])} className='input1' />
        <input type="file" onChange={(e) => setFile2(e.target.files[0])} className='input2' />
        
        <button onClick={handleCompare} className='run-button'>Run Analysis</button>
      </div>

      {result && (
        <div>
          <p>Results Summary</p>
          <p>Score: {result.score}</p>
          <p>Label: {result.label}</p>
          
          <p>Longest phrase: {result.longest_phrase}</p>
          <p>Most common: {result.most_common}</p>
        </div>
      )}
    </div>
  );
}

export default App;