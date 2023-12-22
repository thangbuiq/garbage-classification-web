import { useCallback } from 'react';
import { useDropzone } from 'react-dropzone';
import { Upload } from '../assets';
import axios from 'axios';

const Form = ({ setImage, setIsPending, setUrl, setError }) => {
  const uploadImage = async (image) => {
    setError(false);
    setIsPending(true);

    const formData = new FormData();
    formData.append('file', image);

    try {
      const response = await axios.post(`http://PUBLIC_IP_ADDRESS/upload`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      if (response.status !== 200) {
        throw Error('Internal Server Error');
      }

      const data = response.data;
      setUrl(data.path);
      setIsPending(false);
    } catch (error) {
      console.error('Error:', error);
      setIsPending(false);
      setError(true);
    }
  };

  const onDrop = useCallback(
    async (acceptedFiles) => {
      let file = acceptedFiles[0];
      let reader = new FileReader();

      reader.readAsDataURL(file);
      reader.onload = () => {
        setImage(reader.result);
        uploadImage(file);
      };
    },
    [setImage],
  );

  const { getRootProps, getInputProps, open } = useDropzone({
    onDrop,
    maxFiles: 1,
    accept: { 'image/*': [] },
    noClick: true,
    noKeyboard: true,
  });

  return (
    <div className="flex flex-col min-h-[50vh] sm:drop-shadow-2xl w-full py-16 sm:px-16 sm:py-10 justify-between bg-white mx-4 sm:mx-0 sm:w-4/6 md:w-3/5 lg:w-fit rounded-3xl">
      <p className="text-center font-semibold text-[1.675rem] sm:text-3xl mb-4 uppercase text-[#8BC541]">
        garbage classification
      </p>
      <p className="text-center font-thin text-xs text-slate-400 mb-2">File should be Jpeg , Png...</p>
      <div
        {...getRootProps({
          className:
            'h-52 bg-light-grey border-2 border-green-700 border-dashed rounded-2xl flex flex-col justify-center items-center',
        })}
      >
        <input {...getInputProps({ name: 'image' })} />
        <img
          src={Upload}
          className="max-w-1/3 mx-auto mt-2 w-28 sm:w-24"
          draggable="false"
          style={{ userDrag: 'none' }}
        />
      </div>
      <p className="text-slate-400 md:text-md text-center mt-4 text-sm">Drag & Drop your image here</p>
      <p className="text-center font-normal text-slate-400 text-md mt-2 mb-2">Or</p>
      <button
        onClick={open}
        className="bg-lime-400/40 text-slate-600 font-medium p-1 rounded-xl w-auto mx-auto px-4 py-2 text-md"
      >
        Choose a file
      </button>
    </div>
  );
};

export default Form;
