import { useState } from "react";
import api from "../services/api";

function Chat() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const askQuestion = async () => {
    if (!question.trim()) {
      alert("Please enter a question");
      return;
    }

    setLoading(true);
    setAnswer("");

    try {
      const token = localStorage.getItem("token");

      const res = await api.post(
        "/chat/",
        {
          question: question,
        },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      console.log(res.data);

      if (res.data.answer) {
        setAnswer(res.data.answer);
      } else if (res.data.error) {
        alert(res.data.error);
      } else {
        alert("No response received");
      }
    } catch (err) {
      console.log(err);

      if (err.response) {
        console.log(err.response.data);
        alert(JSON.stringify(err.response.data));
      } else {
        alert(err.message);
      }
    }

    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gray-100 flex justify-center items-center">
      <div className="bg-white shadow-xl rounded-xl p-8 w-[700px]">

        <h1 className="text-3xl font-bold mb-6 text-center">
          Chat with AI
        </h1>

        <textarea
          rows="5"
          placeholder="Ask anything about your uploaded PDF..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          className="border rounded-lg w-full p-4"
        />

        <button
          onClick={askQuestion}
          disabled={loading}
          className="bg-blue-600 hover:bg-blue-700 text-white w-full p-3 rounded-lg mt-5"
        >
          {loading ? "Thinking..." : "Ask AI"}
        </button>

        <div className="mt-8">
          <h2 className="text-2xl font-bold mb-3">
            AI Response
          </h2>

          <div className="border rounded-lg p-4 min-h-[150px] bg-gray-50">
            {answer || "Response will appear here..."}
          </div>
        </div>

      </div>
    </div>
  );
}

export default Chat;