import { useNavigate } from "react-router-dom";

function Dashboard() {

    const navigate = useNavigate();

    const logout = () => {

        localStorage.removeItem("token");

        navigate("/");
    }

    return (

        <div className="min-h-screen bg-gray-100">

            <nav className="bg-blue-700 text-white p-5 flex justify-between">

                <h1 className="text-2xl font-bold">
                    📚 Leucine RAG
                </h1>

                <button
                    onClick={logout}
                    className="bg-red-500 px-4 py-2 rounded"
                >
                    Logout
                </button>

            </nav>

            <div className="grid grid-cols-2 gap-8 p-10">

                <div
                    onClick={() => navigate("/upload")}
                    className="cursor-pointer bg-white rounded-xl shadow-lg p-10 hover:scale-105 transition"
                >
                    <h2 className="text-3xl font-bold">

                        📄 Upload PDF

                    </h2>

                    <p className="mt-4">

                        Upload documents for RAG.

                    </p>

                </div>

                <div
                    onClick={() => navigate("/chat")}
                    className="cursor-pointer bg-white rounded-xl shadow-lg p-10 hover:scale-105 transition"
                >

                    <h2 className="text-3xl font-bold">

                        💬 Chat with AI

                    </h2>

                    <p className="mt-4">

                        Ask questions from uploaded documents.

                    </p>

                </div>

            </div>

        </div>

    )

}

export default Dashboard;