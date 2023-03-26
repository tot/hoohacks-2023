import { RiArrowRightUpLine, RiArrowRightDownLine } from "react-icons/ri"
import cn from "classnames"

interface AccountChangeProps {
   amount: number
   previous: number
}

const AmountChange = ({ amount, previous }: AccountChangeProps) => {
   return (
      <div
         className={cn("text-base flex items-center pb-0.5", {
            "text-green-600": amount > 0,
            "text-red-600": amount < 0,
            "text-neutral-500": amount === 0,
         })}
      >
         {amount > 0 ? <RiArrowRightUpLine className="text-xl" /> : null}
         {amount < 0 ? (
            <RiArrowRightDownLine className="text-xl font-normal" />
         ) : null}
         {amount > 0 ? "+" : null}
         {!amount ? 0 : ((amount / previous) * 100).toFixed(2)}%
      </div>
   )
}

export default AmountChange
