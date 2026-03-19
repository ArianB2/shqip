import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Navbar from './components/Navbar'
import Home from './pages/Home'
import Lessons from './pages/Lessons'
import VocabPractice from './pages/VocabPractice'

export default function App() {
  return (
    <BrowserRouter>
      <div className="min-h-screen flex flex-col">
        <Navbar />
        <main className="flex-1">
          <Routes>
            <Route path="/"           element={<Home />} />
            <Route path="/lessons"    element={<Lessons />} />
            <Route path="/practice"   element={<VocabPractice />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  )
}
