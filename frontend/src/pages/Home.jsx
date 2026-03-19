import { Link } from 'react-router-dom'

export default function Home() {
  return (
    <div className="max-w-4xl mx-auto px-4 py-16">

      {/* Hero */}
      <div className="text-center mb-16">
        <div className="text-6xl mb-6">🦅</div>
        <h1 className="text-5xl font-bold text-gray-900 mb-4">
          Learn Albanian.
          <br />
          <span className="text-albania-red">Both dialects.</span>
        </h1>
        <p className="text-xl text-gray-500 max-w-xl mx-auto mb-8 leading-relaxed">
          Shqip is the only app built specifically for learning Albanian —
          including the Gheg dialect spoken in northern Albania and Kosovo,
          and Tosk, the southern standard form.
        </p>
        <div className="flex items-center justify-center gap-4">
          <Link to="/lessons" className="btn-primary text-base px-8 py-3">
            Start learning
          </Link>
          <Link to="/practice" className="btn-secondary text-base px-8 py-3">
            Practice vocabulary
          </Link>
        </div>
      </div>

      {/* Feature highlights */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {[
          {
            icon: '🗣️',
            title: 'Two dialects',
            desc: 'Learn Gheg and Tosk side by side. See exactly how they differ — and why.',
          },
          {
            icon: '🤖',
            title: 'AI conversation tutor',
            desc: 'Practice speaking with an AI that responds in Albanian and corrects your grammar.',
          },
          {
            icon: '🔊',
            title: 'Native pronunciation',
            desc: 'Hear every word spoken aloud so you learn how Albanian actually sounds.',
          },
        ].map(({ icon, title, desc }) => (
          <div key={title} className="bg-white rounded-xl border border-gray-100 p-6 text-center">
            <div className="text-3xl mb-3">{icon}</div>
            <h3 className="font-semibold text-gray-900 mb-2">{title}</h3>
            <p className="text-sm text-gray-500 leading-relaxed">{desc}</p>
          </div>
        ))}
      </div>

      {/* Dialect explainer */}
      <div className="mt-12 bg-red-50 rounded-2xl p-8 border border-red-100">
        <h2 className="font-bold text-lg text-gray-900 mb-3">
          Why does dialect matter?
        </h2>
        <p className="text-gray-600 leading-relaxed text-sm">
          Albanian has two major dialect groups — <strong>Gheg</strong>, spoken in
          northern Albania, Kosovo, and North Macedonia, and <strong>Tosk</strong>, the
          southern form that became the official standard. They differ in vocabulary,
          pronunciation, and some grammar. If you're learning Albanian to speak with
          Kosovars, you need Gheg. Almost no app teaches this distinction. Shqip does.
        </p>
      </div>

    </div>
  )
}
