interface RightArrowProps {
   onClick?: any
}

const RightArrow = ({ onClick }: RightArrowProps) => {
   return (
      <button
         type="button"
         onClick={() => onClick()}
         className="flex items-center justify-center w-12 z-50 h-12 absolute right-0 top-0 bg-red-500"
      >
         right
      </button>
   )
}

export default RightArrow
