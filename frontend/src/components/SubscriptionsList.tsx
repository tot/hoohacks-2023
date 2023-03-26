import Link from "next/link"
import ScrollContainer from "./ScrollContainer"

interface SubscriptionsListProps {
   // TODO: type this
   subscriptions: any[]
}

const SubscriptionsList = ({ subscriptions }: SubscriptionsListProps) => {
   return (
      <div className="col-span-2 md:col-span-2">
         <div className="flex justify-between items-center pb-4">
            <h2 className="text-2xl text-neutral-900 font-semibold">
               Subscriptions
            </h2>
            <Link href="/subscriptions">
               <p className="text-neutral-700 text-base">Manage</p>
            </Link>
         </div>
         <ScrollContainer className="h-[24rem]">
            {/* subscriptions here */}
            {subscriptions.map((subscription, i) => (
               <div key={i}>
                  <div className="flex justify-between p-4">
                     <div className="flex items-center space-x-4">
                        {/* TODO: Replace with logo/placeholder logo */}
                        <div className="w-8 h-8 rounded-full bg-blue-500" />
                        <div>
                           <p className="text-base font-medium text-neutral-900">
                              Netflix
                           </p>
                           <p className="text-sm text-neutral-500">
                              Renewed on 3/20/2022
                           </p>
                        </div>
                     </div>

                     <p className="text-base text-neutral-900">$11.99</p>
                  </div>
               </div>
            ))}
         </ScrollContainer>
      </div>
   )
}

export default SubscriptionsList
