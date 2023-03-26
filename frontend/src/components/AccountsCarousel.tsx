import { useRef, useState } from "react"
import Carousel from "react-multi-carousel"
import "react-multi-carousel/lib/styles.css"
import AccountCard from "./AccountCard"
import LeftArrow from "./LeftArrow"
import RightArrow from "./RightArrow"

interface AccountsCarouselProps {
   // TODO: Type this
   accounts: any[]
}

const AccountsCarousel = ({ accounts }: AccountsCarouselProps) => {
   const responsive = {
      desktop: {
         breakpoint: { max: 3000, min: 1280 },
         items: 4,
      },
      laptop: {
         breakpoint: { max: 3000, min: 1024 },
         items: 4,
      },
      tablet: {
         breakpoint: { max: 1024, min: 464 },
         items: 2,
      },
      mobile: {
         breakpoint: { max: 464, min: 0 },
         items: 1,
      },
   }

   return (
      //@ts-ignore
      <Carousel
         draggable
         partialVisbile
         responsive={responsive}
         className="pt-2"
         showDots
         renderDotsOutside
         itemClass="p-3"
         arrows={false}
         //  customRightArrow={<RightArrow />}
         //  customLeftArrow={<LeftArrow />}
      >
         {accounts.map((account) => (
            <AccountCard key={account.name} {...account} />
         ))}
      </Carousel>
   )
}

export default AccountsCarousel
