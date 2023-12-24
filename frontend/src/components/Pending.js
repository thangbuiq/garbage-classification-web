import '../app.css';
const Pending = () => {
  return (
    <div className="flex flex-col drop-shadow-lg p-5 justify-between bg-white w-4/5 md:w-2/6 rounded-md">
      <p className="text-sm w-15 mb-5 font-semibold">ProEnv is giving advice...</p>
      <div className="w-full p-0 h-1 bg-grey mb-5 relative">
        <div className="absolute w-0 loader bg-lime-400 h-1" />
      </div>
    </div>
  );
};

export default Pending;
