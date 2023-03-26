interface LeftArrowProps {
   onClick?: any
}

const LeftArrow = ({ onClick }: LeftArrowProps) => {
   return (
      <button
         type="button"
         onClick={() => onClick()}
         className="flex items-center justify-center w-8 h-8 rounded-full absolute -left-2 top-1/2 -translate-y-1/2 bg-red-500"
      >
         {"<"}
      </button>
   )
}

export default LeftArrow
