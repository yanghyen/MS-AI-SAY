import React from "react";
import PropTypes from "prop-types";

const MyCssFirst = (props) => {
    const tblDesign = {
        color: props.c,
        backgroundColor: props.bgc,
        width : props.w+"px",
    };

    return (
        <table border={1} style={tblDesign}>
            <tr>
                <td>{props.bgc}</td>
            </tr>
            <tr>
                <td>{props.c}</td>
            </tr>
        </table>
    );
};

MyCssFirst.propTypes = {
    c: PropTypes.string.isRequired,
    bgc: PropTypes.string.isRequired,
    w: PropTypes.number.isRequired
};

export default MyCssFirst;
