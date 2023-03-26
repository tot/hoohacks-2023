import { RiArrowRightUpLine, RiArrowRightDownLine } from "react-icons/ri"
import cn from "classnames"

interface AccountChangeProps {
   amount: string
}

const AmountChange = ({ amount }: AccountChangeProps) => {
   return (
      <div
         className={cn("text-base flex items-center pb-0.5", {
            "text-green-600": amount[0] === "+",
            "text-red-600": amount[0] === "-",
            "text-neutral-500":
               amount.substring(0, amount.length - 1) === "0.00",
         })}
      >
         {amount[0] === "+" ? <RiArrowRightUpLine className="text-xl" /> : null}
         {amount[0] === "-" ? (
            <RiArrowRightDownLine className="text-xl font-normal" />
         ) : null}
         {amount}
      </div>
   )
}

export default AmountChange
