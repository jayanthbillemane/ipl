const url="http://127.0.0.1:5000/latest_match_winner";
const editPost=document.getElementById('edit');

const renderPost=(r)=>{
console.log("Detazz",r)
let tab = 
            `<tr>
            <th>City</th>
            <th>Date</th>
            <th>Venue</th>
            <th>Team1</th>
            <th>Team2</th>
            <th>Toss Winner</th>
            <th>Toss Decision</th>
            <th>Winner</th>
            <th>Player of the Match</th>
            <th>neutral_venue</th>
            <th>result</th>
            <th>result_margin</th>
            <th>eliminator</th>
            <th>method</th>
            <th>umpire1</th>
            <th>umpire2</th>
            
            </tr>`;
    

        tab += `<tr> 
        <td>${r.city} </td> 
        <td>${r.date} </td>        
        <td>${r.venue} </td>        
        <td>${r.team1} </td>        
        <td>${r.team2} </td>        
        <td>${r.toss_winner} </td>        
        <td>${r.toss_decision} </td>        
        <td>${r.winner} </td> 
        <td>${r.player_of_match} </td>
        
        <td>${r.neutral_venue} </td> 
        <td>${r.result} </td>
        <td>${r.result_margin} </td> 
        <td>${r.eliminator} </td>   
        <td>${r.method} </td>             
        <td>${r.umpire1} </td> 
        <td>${r.umpire2} </td>             


        </tr>`;
    // }
    document.getElementById("iplLastMatchDetail").innerHTML = tab;

}

fetch(url)
.then(res=>res.json())
.then(data=>{
renderPost(data)
})
