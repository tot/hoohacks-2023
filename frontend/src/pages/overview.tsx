import AccountsCarousel from "@/components/AccountsCarousel"
import Header from "@/components/Header"
import SubscriptionsList from "@/components/SubscriptionsList"
import DashboardLayout from "@/layouts/DashboardLayout"
import { useEffect, useState } from "react"

const Dashboard = () => {
   // TODO: Type this
   const [accounts, setAccounts] = useState<any[]>([])
   const [subscriptions, setSubscriptions] = useState<any[]>([])

   useEffect(() => {
      Promise.all([
         fetch(
            "https://hoohacks.herokuapp.com/api/subscriptions?customer_id=64204b0c78f6910a15f0e5aa"
         ),
         fetch(
            "https://hoohacks.herokuapp.com/api/stats?customer_id=64204b0c78f6910a15f0e5aa"
         ),
      ])
         .then(([resSubscriptions, resStats]) =>
            Promise.all([resSubscriptions.json(), resStats.json()])
         )
         .then(([dataSubscriptions, dataStats]) => {
            setSubscriptions(dataSubscriptions)
            setAccounts(dataStats)
         })
   }, [])

   return (
      <DashboardLayout>
         <Header
            title="Overview"
            description="View all your personal financial analytics and details"
         />
         <h2 className="text-2xl text-neutral-900 font-semibold pt-6">
            Accounts
         </h2>
         <div className="w-full relative pb-6">
            <AccountsCarousel accounts={accounts} />
         </div>
         <div className="grid grid-cols-2 md:grid-cols-2 lg:grid-cols-3 gap-6 pt-6">
            <SubscriptionsList subscriptions={subscriptions} />
            <div className="col-span-2 md:col-span-1 lg:col-span-2">
               <div className="flex justify-between items-center pb-4">
                  <h2 className="text-2xl text-neutral-900 font-semibold">
                     Spending Habits
                  </h2>
                  {/* <p className="text-neutral-700 text-base">
                     View recommendations
                  </p> */}
               </div>
            </div>
         </div>
      </DashboardLayout>
   )
}

export default Dashboard
