import { useState } from 'react'

/**
 * useDialect — manages which Albanian dialect the user has selected.
 *
 * Returns the current dialect and a toggle function.
 * Usage:
 *   const { dialect, toggleDialect, setDialect } = useDialect()
 *
 * Month 2: persist this to the user's profile in the database instead of local state.
 */
export function useDialect(initial = 'tosk') {
  const [dialect, setDialect] = useState(initial)

  const toggleDialect = () =>
    setDialect((prev) => (prev === 'tosk' ? 'gheg' : 'tosk'))

  return { dialect, toggleDialect, setDialect }
}
