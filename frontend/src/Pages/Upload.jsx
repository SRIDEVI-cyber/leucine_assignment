import { useState } from "react";

function Upload() {
  const [file, setFile] =useState(null);

  return (
    <div style={{ padding: "50px" }}>
      <h1>Upload PDF</h1>

      <input
        type="file"
        accept=".pdf"
        onChange={(e) => {
          console.log(e.target.files);
          setFile(e.target.files[0]);
        }}
      />

      <br /><br />

      <button
        type="button"
        onClick={() => console.log(file)}
      >
        Upload
      </button>
    </div>
  );
}

export default Upload;