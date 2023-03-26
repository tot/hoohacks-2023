import Navbar from "@/components/Navbar"
import { ReactNode } from "react"

interface DashboardLayoutProps {
   children: ReactNode
}

const DashboardLayout = ({ children }: DashboardLayoutProps) => {
   return (
      <main className="w-full min-h-screen bg-neutral-100 flex flex-1 flex-col">
         <Navbar />
         <div className="max-w-7xl mx-auto p-4 flex flex-1 flex-col w-full">
            {children}
         </div>
      </main>
   )
}

export default DashboardLayout
