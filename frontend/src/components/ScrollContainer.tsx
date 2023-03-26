import { ReactNode } from "react"
import cn from "classnames"

interface ScrollContainerProps {
   children: ReactNode
   className?: string
}

const ScrollContainer = ({ children, className }: ScrollContainerProps) => {
   return (
      <div
         className={cn(
            className,
            "border border-neutral-300 bg-zinc-50 shadow rounded-xl overflow-y-auto divide-y divide-neutral-200"
         )}
      >
         {children}
      </div>
   )
}

ScrollContainer.defaultProps = {
   className: null,
}

export default ScrollContainer
