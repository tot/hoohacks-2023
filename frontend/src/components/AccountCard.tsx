import AmountChange from "./AmountChange"

interface AccountCardProps {
   type: string
   current_balance: number
   last_balance: number
}

const AccountCard = ({
   type,
   current_balance,
   last_balance,
}: AccountCardProps) => {
   return (
      <div className="w-full h-full p-4 bg-zinc-50 rounded-xl shadow border border-neutral-300 select-none">
         <p className="text-base text-neutral-700 pb-1">{type}</p>
         <p className="text-xl font-semibold flex items-end space-x-1">
            <span className="">${current_balance}</span>
            <AmountChange
               amount={current_balance - last_balance}
               previous={last_balance}
            />
         </p>
      </div>
   )
}

export default AccountCard
