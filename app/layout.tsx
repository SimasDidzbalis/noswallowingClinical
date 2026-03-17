export const metadata = {
  title: "NoSwallowing.com",
  description: "Clinical adherence hub powered by Nutrioz",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
