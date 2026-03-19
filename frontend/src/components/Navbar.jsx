import { Link, useLocation } from 'react-router-dom'
import { useState } from 'react'
import DialectToggle from './DialectToggle'

export default function Navbar() {
  const location = useLocation()
  const [dialect, setDialect] = useState('tosk')

  const navLinks = [
    { to: '/',         label: 'Home' },
    { to: '/lessons',  label: 'Lessons' },
    { to: '/practice', label: 'Practice' },
  ]

  return (
    <nav className="bg-white border-b border-gray-100 sticky top-0 z-50">
      <div className="max-w-6xl mx-auto px-4 h-16 flex items-center justify-between">

        {/* Logo */}
        <Link to="/" className="flex items-center gap-2">
          {/* Albanian eagle — simplified Unicode stand-in until you add a real SVG icon */}
          <span className="text-2xl">🦅</span>
          <span className="font-bold text-xl text-albania-red tracking-tight">
            Shqip
          </span>
          <span className="text-xs text-gray-400 font-normal hidden sm:block">
            Learn Albanian
          </span>
        </Link>

        {/* Nav links */}
        <div className="hidden md:flex items-center gap-6">
          {navLinks.map(({ to, label }) => (
            <Link
              key={to}
              to={to}
              className={`text-sm font-medium transition-colors ${
                location.pathname === to
                  ? 'text-albania-red'
                  : 'text-gray-600 hover:text-gray-900'
              }`}
            >
              {label}
            </Link>
          ))}
        </div>

        {/* Dialect toggle + auth placeholder */}
        <div className="flex items-center gap-3">
          <DialectToggle dialect={dialect} onToggle={() =>
            setDialect(d => d === 'tosk' ? 'gheg' : 'tosk')
          } />
          {/* Month 2: replace this with real login button */}
          <button className="btn-secondary text-sm hidden sm:block">
            Sign in
          </button>
        </div>

      </div>
    </nav>
  )
}
