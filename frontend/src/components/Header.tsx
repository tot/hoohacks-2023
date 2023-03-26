interface HeaderProps {
   title: string
   description: string
}

const Header = ({ title, description }: HeaderProps) => {
   return (
      <div className="pt-4">
         <h1 className="text-3xl font-semibold text-neutral-900">{title}</h1>
         <p className="text-base text-neutral-500">{description}</p>
      </div>
   )
}

export default Header
