//import CheckIcon from '@mui/icons-material/Check';
const Uploaded = ({ image, url }) => {
  return (
    <div className="flex flex-col sm:drop-shadow-lg gap-6 py-16 items-center justify-center w-full mx-4 bg-white md:w-3/5 rounded-md">
      <p className="text-center font-semibold text-2xl uppercase text-[#8BC541]">garbage classification</p>
      <div>
        <img src={image} className="max-w-full mx-auto h-[18vh] sm:h-[28vh] rounded-3xl" />
      </div>
      <div className="flex justify-center">
        <div className="capitalize bg-lime-400/40 text-slate-600 text-md rounded-xl px-8 py-3 ml-4 mr-4">
          Advice for user Advice for user Advice for user Advice for user Advice for user Advice for user Advice for
          user Advice for user Advice for user Advice for user Advice for user Advice for user Advice for user Advice
          for user Advice for user Advice for user Advice for user Advice for user Advice for user Advice for user
          Advice for user Advice for user Advice for user Advice for user Advice for user{' '}
        </div>
      </div>
    </div>
  );
};

export default Uploaded;
