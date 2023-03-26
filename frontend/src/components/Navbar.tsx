import Link from "next/link"
import cn from "classnames"
import { useRouter } from "next/router"

const LINKS = [
   {
      name: "Overview",
      slug: "/overview",
   },
   {
      name: "Assistant",
      slug: "/assistant",
   },
]

const Navbar = () => {
   const router = useRouter()
   return (
      <div className="w-full border-b border-neutral-200 bg-zinc-50 shadow">
         <div className="max-w-7xl mx-auto md:flex md:items-center md:justify-between p-4 space-y-4 md:space-y-0">
            <h1 className="text-neutral-900 text-xl font-semibold">
               Pennywise<span className="font-bold text-blue-500">.</span>
            </h1>
            <div className="md:flex md:items-center md:space-x-4">
               {LINKS.map(({ name, slug }) => (
                  <Link key={name} href={slug}>
                     <h3
                        className={cn("p-2", "rounded-lg", {
                           "bg-blue-100 text-blue-600":
                              router.pathname === slug,
                           "text-neutral-900 hover:bg-neutral-100":
                              router.pathname !== slug,
                        })}
                     >
                        {name}
                     </h3>
                  </Link>
               ))}
            </div>
            <div className="flex items-center space-x-4">
               <p className="text-base">Hello, John</p>
               <div
                  className="w-10 h-10 bg-blue-500 rounded-full bg-cover bg-center"
                  style={{
                     backgroundImage: `url("https://images.unsplash.com/photo-1517849845537-4d257902454a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1035&q=80")`,
                  }}
               />
            </div>
         </div>
      </div>
   )
}

export default Navbar
