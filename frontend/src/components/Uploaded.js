//import CheckIcon from '@mui/icons-material/Check';
const Uploaded = ({ image, url }) => {
  const copy = async () => {
    await navigator.clipboard.writeText(url);
    alert('Link copied');
  };

  return (
    <div className="flex flex-col sm:drop-shadow-lg gap-8 py-16 items-center justify-center w-full mx-4 bg-white md:w-3/5 rounded-md">
      <p className="text-center font-semibold text-3xl mb-4 uppercase text-[#8BC541]">garbage classification</p>
      <div>
        <img src={image} className="max-w-full mx-auto h-[30vh] rounded-2xl" />
      </div>
      <div className="flex justify-center">
        <button onClick={copy} className="capitalize bg-lime-400/40 text-slate-600 text-md rounded-xl px-8 py-3">
          copy
        </button>
      </div>
    </div>
  );
};

export default Uploaded;
