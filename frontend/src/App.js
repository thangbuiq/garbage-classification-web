import { useState } from 'react';
import Form from './components/Form';
import Pending from './components/Pending';
import Uploaded from './components/Uploaded';
import { Logo, Earth } from './assets';

function App() {
  const [isPending, setIsPending] = useState(false);
  const [image, setImage] = useState(null);
  const [url, setUrl] = useState(null);
  const [error, setError] = useState(false);
  return (
    <div className="w-full h-screen bg-grey flex justify-center items-center relative">
      <img src={Logo} className='absolute top-4 left-4 w-52' />
      {error ? (
        <p className="text-red-600 text-center border-red-600 rounded-lg border-2 bg-red-300 px-4 py-2">
          internal server error , Refresh the page and try again
        </p>
      ) : isPending ? (
        <Pending />
      ) : image && url ? (
        <Uploaded image={image} url={url} />
      ) : (
        <Form image={image} setImage={setImage} setIsPending={setIsPending} setUrl={setUrl} setError={setError} />
      )}
      <img src={Earth} className='absolute bottom-4 right-4 w-64' />
    </div>
  );
}

export default App;
