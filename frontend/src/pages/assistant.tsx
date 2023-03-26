import Header from "@/components/Header"
import DashboardLayout from "@/layouts/DashboardLayout"

const Dashboard = () => {
   return (
      <DashboardLayout>
         <Header
            title="Assistant"
            description="Talk to a personalized financial advisor about your banking activity."
         />
         <h2 className="text-2xl text-neutral-900 font-semibold pt-6">
            Accounts
         </h2>
         <div className="gap-6 pt-6"></div>
      </DashboardLayout>
   )
}

export default Dashboard
