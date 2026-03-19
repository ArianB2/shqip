/**
 * DialectToggle
 * The signature UI element of Shqip — lets the user switch between
 * Gheg (northern) and Tosk (standard/southern) Albanian.
 *
 * Props:
 *   dialect  — 'gheg' | 'tosk'
 *   onToggle — function called when the user clicks
 */
export default function DialectToggle({ dialect, onToggle }) {
  const isGheg = dialect === 'gheg'

  return (
    <button
      onClick={onToggle}
      className="flex items-center gap-1 bg-gray-100 rounded-full px-3 py-1.5
                 hover:bg-gray-200 transition-colors text-sm font-medium"
      title="Switch Albanian dialect"
    >
      <span className={isGheg ? 'text-gray-400' : 'text-albania-red font-semibold'}>
        Tosk
      </span>
      <span className="text-gray-300 mx-1">|</span>
      <span className={isGheg ? 'text-albania-red font-semibold' : 'text-gray-400'}>
        Gheg
      </span>
    </button>
  )
}
