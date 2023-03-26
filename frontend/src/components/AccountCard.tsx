import AmountChange from "./AmountChange"

interface AccountCardProps {
   name: string
   balance: string
   change: string
}

const AccountCard = ({ name, balance, change }: AccountCardProps) => {
   return (
      <div className="w-full h-full p-4 bg-zinc-50 rounded-xl shadow border border-neutral-300 select-none">
         <p className="text-base text-neutral-700 pb-1">{name}</p>
         <p className="text-xl font-semibold flex items-end space-x-1">
            <span className="">${balance}</span>
            <AmountChange amount={change} />
         </p>
      </div>
   )
}

export default AccountCard
