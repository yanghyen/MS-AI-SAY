import React from 'react'
import PropTypes from 'prop-types'

const MyPropsSecond = props => {
  return (
    <>
        <h3>{props.namee}</h3>
        <h3>{props.pricee}</h3>
    </>
  )
}

MyPropsSecond.propTypes = {
    namee : PropTypes.string.isRequired,   // ptsr
    pricee : PropTypes.number
}

export default MyPropsSecond