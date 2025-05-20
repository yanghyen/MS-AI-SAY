import React, { useEffect } from 'react'

const MySocketClnt = () => {
    useEffect(() => {
      window.io.connect("http://localhost:8787");
    }, [])
    
  return (
    <div>MySocketClnt</div>
  )
}

export default MySocketClnt