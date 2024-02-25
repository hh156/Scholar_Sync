// Sample leaderboard data (replace with your own data)
var leaderboardData = [
  { username: "user1", points: 100 },
  { username: "user2", points: 80 },
  { username: "user3", points: 120 },
  { username: "user4", points: 90 },
  { username: "user5", points: 110 },
  { username: "user6", points: 70 },
  { username: "user7", points: 130 },
  { username: "user8", points: 85 },
  { username: "user9", points: 115 },
  { username: "user10", points: 95 }
  // Add more entries as needed
];

// Function to render leaderboard
function renderLeaderboard() {
  var leaderboardBody = document.getElementById('leaderboardBody');
  leaderboardBody.innerHTML = '';

  leaderboardData.sort((a, b) => b.points - a.points); // Sort entries by points

  leaderboardData.forEach((entry, index) => {
    var row = leaderboardBody.insertRow();
    var rankCell = row.insertCell(0);
    var usernameCell = row.insertCell(1);
    var pointsCell = row.insertCell(2);
    rankCell.textContent = index + 1;
    usernameCell.textContent = entry.username;
    pointsCell.textContent = entry.points;
  });
}

// Initial rendering
renderLeaderboard();
