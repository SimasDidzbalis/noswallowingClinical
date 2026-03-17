export default function Home() {
  return (
    <main className="page">
      <section className="hero">
        <div className="hero-inner">
          <p className="eyebrow">Clinical adherence hub powered by Nutrioz</p>
          <h1>
            When swallowing is the barrier, adherence breaks.
          </h1>
          <p className="subtext">
            Nutrioz Oral Spray is a non-swallowing supplementation pathway for
            dysphagia patients, bariatric patients, elderly users, and anyone
            who struggles with pills or capsules.
          </p>

          <div className="cta-row">
            <a className="btn btn-primary" href="https://nutrioz.com">
              Try Nutrioz
            </a>
            <a className="btn btn-secondary" href="#refer">
              Refer a patient
            </a>
          </div>
        </div>
      </section>

      <section className="problem">
        <div className="container">
          <p className="section-label">The problem</p>
          <h2>Swallowing-dependent supplementation creates avoidable failure.</h2>
          <p className="section-text">
            Dysphagia, bariatric recovery, aging, pill fatigue, and routine
            non-compliance all reduce the probability that patients will follow
            traditional oral supplementation consistently.
          </p>
        </div>
      </section>

      <section className="solution">
        <div className="container">
          <p className="section-label">The solution</p>
          <h2>Nutrioz Oral Spray bypasses swallowing completely.</h2>
          <p className="section-text">
            A 0.06 ml precision oral spray designed to remove swallowing from
            the supplementation process.
          </p>
        </div>
      </section>

      <section className="audiences">
        <div className="container">
          <p className="section-label">Who this is for</p>
          <div className="cards">
            <div className="card">
              <h3>Dysphagia patients</h3>
              <p>For cases where swallowing itself is the barrier.</p>
            </div>
            <div className="card">
              <h3>Bariatric patients</h3>
              <p>For post-surgical routines with higher adherence friction.</p>
            </div>
            <div className="card">
              <h3>Elderly users</h3>
              <p>For people who avoid, forget, or struggle with tablets.</p>
            </div>
          </div>
        </div>
      </section>

      <section className="refer" id="refer">
        <div className="container refer-box">
          <div>
            <p className="section-label">Referral</p>
            <h2>Need a clinician referral workflow?</h2>
            <p className="section-text">
              This page is the front-end entry point for dysphagia and bariatric
              adherence pathways. Next step is adding referral and partner logic.
            </p>
          </div>

          <div className="cta-row">
            <a className="btn btn-primary" href="https://nutrioz.com">
              View product
            </a>
            <a className="btn btn-secondary" href="mailto:simas@no-swallowing.com">
              Contact
            </a>
          </div>
        </div>
      </section>
    </main>
  )
}
