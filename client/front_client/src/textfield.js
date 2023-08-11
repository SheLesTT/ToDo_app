import React, { useState } from 'react';

function TextField() {
  const [textValue, setTextValue] = useState('');

  const handleInputChange = (event) => {
    setTextValue(event.target.value);
  };

  return (
    <div>
      <input
        type="text"
        value={textValue}
        onChange={handleInputChange}
        placeholder="Enter text here"
      />
      <p>You entered: {textValue}</p>
    </div>
  );
}

export default TextField;
