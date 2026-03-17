export default function Page(){
  return (
    <main style={{background:"#000",color:"#fff",minHeight:"100vh",padding:"40px"}}>
      <h1 style={{fontSize:"48px"}}>NoSwallowing.com</h1>
      <p style={{marginTop:"20px",fontSize:"20px"}}>
        When swallowing is the barrier, adherence breaks.
      </p>

      <div style={{marginTop:"40px"}}>
        <h2>Clinical Use Cases</h2>
        <ul>
          <li>Dysphagia patients</li>
          <li>Bariatric patients</li>
          <li>Elderly compliance</li>
        </ul>
      </div>

      <div style={{marginTop:"40px"}}>
        <button style={{padding:"12px 20px",background:"#fff",color:"#000",borderRadius:"10px"}}>
          Refer a Patient
        </button>
      </div>
    </main>
  )
}
