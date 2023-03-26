import Header from "@/components/Header"
import DashboardLayout from "@/layouts/DashboardLayout"
import { useState, ChangeEvent } from "react"
import getCompletion from "@/chat/openAI"

const getTransactions = async () => {
   const res = await fetch(
      "http://127.0.0.1:5000/api/transactions?customer_id=64204b0c78f6910a15f0e5aa"
   )
   const data = await res.json()
   return data
}

const Dashboard = () => {
   const [message, setMessage] = useState("")
   const [displayMessage, setDisplayMessage] = useState("")
   const [response, setResponse] = useState("")
   const [isLoading, setLoading] = useState(false)

   const onClickHandler = async () => {
      setDisplayMessage(message)
      setLoading(true)

      const txns = await getTransactions()
      console.log(txns)
      const res = await fetch("https://api.openai.com/v1/chat/completions", {
         headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer {apiKey}`,
         },
         method: "POST",
         body: JSON.stringify({
            model: "gpt-3.5-turbo",
            messages: [
               {
                  role: "system",
                  content:
                     // 			   You are a financial advisor. Given transaction data from the past week as follows:
                     // McDonalds, 50 dollars
                     // Chick fil a, 40 dollars
                     // Target, 10 dollars
                     // How can I save 100 dollars over the next week? Give advice tailored for me by looking at the company names and amount spent. Be as specific as possible.
                     "You are a financial assistant helping people manage their money." +
                     "People have the goal of saving money and reducing their spending." +
                     "You are given a JSON stringified list of their recent transactions containing the merchant they bought from, how much they spent, and the date of the transaction. " +
                     "Based on these transactions, provide advice for how they can save money over the next month.",
               },
               {
                  role: "user",
                  content: JSON.stringify(txns),
               },
            ],
            max_tokens: 200,
            temperature: 0.3,
            presence_penalty: 0.2, //change to 1 for more creative, when doing more than 1 category
            frequency_penalty: 0.2,
            // stream: false,
         }),
      })
      const data = await res.json()
      const result = data.choices[0].message.content
      console.log(result)
      setResponse(result)
      setLoading(false)
   }

   return (
      <DashboardLayout>
         <Header
            title="Assistant"
            description="Talk to a personalized financial advisor about your banking activity."
         />
         <div className="space-y-4 pt-8">
            <div className="bg-gray-200 p-4 rounded-xl text-neutral-900 mx-auto max-w-2xl w-full h-full mt-4 text-center max-h-[24rem] overflow-y-auto">
               {displayMessage ? (
                  <p>
                     <span className="font-medium">Your question: </span>
                     {displayMessage}
                  </p>
               ) : (
                  "Send a question to get started"
               )}
            </div>
            {isLoading ? (
               <div className="mx-auto text-center text-neutral-500">
                  <p>Generating response...</p>
               </div>
            ) : response ? (
               <div className="bg-gray-200 p-4 rounded-xl text-neutral-900 mx-auto max-w-2xl w-full h-full mt-4 text-center">
                  {response ? `Response: ${response}` : null}
               </div>
            ) : null}
         </div>
         <div className="mt-auto mx-auto min-w-[24rem] pb-6 flex items-center space-x-2">
            <input
               className="p-2 bg-gray-200 w-full rounded-xl focus:outline-blue-500 focus:outline-2"
               placeholder="Ask us a question"
               onChange={(event: ChangeEvent<HTMLInputElement>) =>
                  setMessage(event.target.value)
               }
            />
            <button
               className="px-4 py-2 bg-blue-500 hover:bg-blue-600 text-zinc-50 rounded-xl"
               onClick={() => onClickHandler()}
            >
               Send
            </button>
         </div>
      </DashboardLayout>
   )
}

export default Dashboard
