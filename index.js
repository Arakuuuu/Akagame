const readline = require('readline');
const MalwareScanner = require('./lib/malwareScanner');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

async function handleMalwareScan() {
  const scanner = new MalwareScanner(process.cwd());
  const suspiciousFiles = await scanner.scanFiles();

  if (suspiciousFiles.length > 0) {
    console.log('\nWould you like to delete any suspicious files?');
    console.log('Enter the number of the file to delete, or 0 to skip:');
    
    const answer = await new Promise(resolve => {
      rl.question('Choice: ', resolve);
    });

    const fileIndex = parseInt(answer) - 1;
    if (fileIndex >= 0 && fileIndex < suspiciousFiles.length) {
      const file = suspiciousFiles[fileIndex];
      console.log(`\nWarning: You are about to delete: ${file.path}`);
      console.log('Risk Level:', file.riskLevel);
      console.log('Detected Threats:');
      file.threats.forEach(threat => console.log(`- ${threat}`));
      
      const confirm = await new Promise(resolve => {
        rl.question('\nAre you sure you want to delete this file? (yes/no): ', resolve);
      });

      if (confirm.toLowerCase() === 'yes') {
        const deleted = await scanner.deleteFile(file.path);
        if (deleted) {
          console.log(`File deleted successfully: ${file.path}`);
        } else {
          console.log(`Failed to delete file: ${file.path}`);
        }
      } else {
        console.log('File deletion cancelled.');
      }
    }
  }
}

async function main() {
  console.log(`\nWelcome to Advanced Security Scanner v1.0`);
  
  while (true) {
    console.log('\n1. Check URL Safety');
    console.log('2. Check Password Strength');
    console.log('3. Encrypt/Decrypt File');
    console.log('4. Scan for Malware');
    console.log('5. Exit');
    
    const answer = await new Promise(resolve => {
      rl.question('\nSelect an option (1-5): ', resolve);
    });

    switch (answer) {
      case '4':
        await handleMalwareScan();
        break;
      case '5':
        console.log('Exiting...');
        rl.close();
        process.exit(0);
        break;
      default:
        console.log('This option is not implemented in the Node.js version.');
        break;
    }
  }
}

main().catch(console.error);
