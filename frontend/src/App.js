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

  const handleRetry = () => {
    setError(false);
    setIsPending(false);
  };

  return (
    <div className="w-full h-[100vh] bg-white sm:bg-grey flex justify-center items-center">
      <img src={Logo} className="absolute top-4 left-4 sm:top-6 sm:left-6 w-40" />
      {error ? (
        <div className="flex flex-col items-center gap-4 drop-shadow-2xl bg-white px-20 py-10 rounded-2xl">
          <p className="text-red-600 text-md rounded-2xl bg-red-200 px-9 py-3">
            Contact the developer, the server is down :D
          </p>
          <button
            onClick={handleRetry}
            className="bg-lime-400/40 text-slate-600 font-medium rounded-xl w-auto mx-auto px-6 py-3 text-md"
          >
            Retry
          </button>
        </div>
      ) : isPending ? (
        <Pending />
      ) : image && url ? (
        <Uploaded image={image} url={url} />
      ) : (
        <Form image={image} setImage={setImage} setIsPending={setIsPending} setUrl={setUrl} setError={setError} />
      )}
      <img src={Earth} className="absolute bottom-0 right-0 w-28 sm:bottom-4 sm:right-4 sm:w-64" />
    </div>
  );
}

export default App;
