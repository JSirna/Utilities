const fileInput = document.getElementById('fileInput');

fileInput.addEventListener('change', (event) => {
  const file = event.target.files[0];
  const reader = new FileReader();

  reader.onload = (event) => {
    const fileContents = event.target.result;
    console.log('File contents:', fileContents);
    const para = document.createElement("p");
    const node = document.createTextNode(fileContents);
    para.appendChild(node);
    const element = document.getElementById("div1");
    element.appendChild(para);
  };

  reader.readAsText(file);
});