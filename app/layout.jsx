import './globals.css'

export const metadata = {
  title: 'NoSwallowing.com',
  description: 'Clinical adherence hub powered by Nutrioz',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
