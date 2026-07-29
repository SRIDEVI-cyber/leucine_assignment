import { Link } from "react-router-dom";

function Register() {
  return (
    <div className="min-h-screen bg-gradient-to-r from-green-500 to-blue-600 flex items-center justify-center">

      <div className="bg-white p-8 rounded-xl shadow-xl w-[400px]">

        <h1 className="text-3xl font-bold text-center mb-6">
          Create Account
        </h1>

        <input
          placeholder="Username"
          className="w-full border p-3 rounded-lg mb-4"
        />

        <input
          placeholder="Email"
          className="w-full border p-3 rounded-lg mb-4"
        />

        <input
          type="password"
          placeholder="Password"
          className="w-full border p-3 rounded-lg mb-6"
        />

        <button className="bg-green-600 w-full text-white p-3 rounded-lg">
          Register
        </button>

        <p className="text-center mt-5">
          Already have an account?{" "}
          <Link to="/" className="text-blue-600">
            Login
          </Link>
        </p>

      </div>

    </div>
  );
}

export default Register;