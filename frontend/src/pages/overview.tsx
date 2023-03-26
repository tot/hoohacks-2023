import AccountsCarousel from "@/components/AccountsCarousel"
import Header from "@/components/Header"
import SubscriptionsList from "@/components/SubscriptionsList"
import DashboardLayout from "@/layouts/DashboardLayout"

const accounts = [
   {
      name: "Checking **4432",
      balance: "230.32",
      transactions: 2332,
      change: "+44%",
   },
   {
      name: "Savings **2334",
      balance: "230.32",
      transactions: 2332,
      change: "-22%",
   },
   {
      name: "Credit Card **8839",
      balance: "8934.03",
      transactions: 2332,
      change: "0.00%",
   },
   {
      name: "Checking **2330",
      balance: "8934.03",
      transactions: 2332,
      change: "-12%",
   },
]

const subscriptions = [
   {
      merchantName: "hi",
      cost: 32.99,
      renewed: "3/22/23",
   },
   {
      merchantName: "hi",
      cost: 32.99,
      renewed: "3/22/23",
   },
   {
      merchantName: "hi",
      cost: 32.99,
      renewed: "3/22/23",
   },
]

const Dashboard = () => {
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
         <div className="grid grid-cols-3 gap-6 pt-6">
            <SubscriptionsList subscriptions={subscriptions} />
            <div className="col-span-2">
               <div className="flex justify-between items-center pb-4">
                  <h2 className="text-2xl text-neutral-900 font-semibold">
                     Spending Habits
                  </h2>
                  <p className="text-neutral-700 text-base">
                     View recommendations
                  </p>
               </div>
            </div>
         </div>
      </DashboardLayout>
   )
}

export default Dashboard
