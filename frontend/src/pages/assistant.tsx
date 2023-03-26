import Header from "@/components/Header"
import DashboardLayout from "@/layouts/DashboardLayout"
import { useState, ChangeEvent } from "react"

const Dashboard = () => {
   const [message, setMessage] = useState("")
   const [displayMessage, setDisplayMessage] = useState("")
   const [response, setResponse] = useState("")
   const [isLoading, setLoading] = useState(true)

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
               onClick={() => setDisplayMessage(message)}
            >
               Send
            </button>
         </div>
      </DashboardLayout>
   )
}

export default Dashboard
